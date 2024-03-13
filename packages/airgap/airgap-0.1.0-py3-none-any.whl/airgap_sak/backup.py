#!/usr/bin/env python3
import subprocess
import argparse
import time
import os
import sys

CVD_DIR = f"{os.getenv('PWD')}/clamav-db"

def check_config():
    if not os.path.exists(os.path.join(CVD_DIR, "config.json")):
        print("Missing CVD configuration. Creating...")
        subprocess.run(["python3", "-m", "cvdupdate", "config", "set", "--config", os.path.join(CVD_DIR, "config.json"), "--dbdir", os.path.join(CVD_DIR, "databases"), "--logdir", os.path.join(CVD_DIR, "logs")])
        print("CVD configuration created...")
    if not os.path.exists(os.path.join(CVD_DIR, "databases")):
        print(f"Creating {os.path.join(CVD_DIR, 'databases')} folder")
        os.makedirs(os.path.join(CVD_DIR, "databases"))

def show_config():
    print("CVD-Update configuration...")
    subprocess.run(["python3", "-m", "cvdupdate", "config", "show", "--config", os.path.join(CVD_DIR, "config.json")])
    print(f"Current contents in {os.path.join(CVD_DIR, 'databases')} directory...")
    subprocess.run(["ls", "-al", os.path.join(CVD_DIR, "databases")])

def update_database():
    print("Updating ClamAV Database...")
    subprocess.run(["python3", "-m", "cvdupdate", "update", "--config", os.path.join(CVD_DIR, "config.json")])
    print("ClamAV Database updated...")

def get_deployments(namespace):
    print("Get Anchore deployments...")
    try:
        result = subprocess.run(['kubectl', 'get', 'deployments', '-n', namespace], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')[1:]
        deployments = [f"{line.split()[0]}_{line.split()[1]}" for line in lines]
        return deployments
    except subprocess.CalledProcessError:
        print(f"Error: Unable to list deployments in the '{namespace}' namespace.")
        exit(2)

def scale(namespace, method, deployments, replicas):
    print(f"Scaling {'up' if method == 'up' else 'down'} deployments...")
    for dep in deployments:
        name = dep.split('_')[0]
        if replicas == 0:
            replicas = dep.split('/')[-1]
        scale = 0 if method == 'down' else replicas

        match = False

        # Deployments to match for when the feeds database is selected
        if feeddb:
            match = "enterprise-feeds" in name

        if match:
            print(f" - {name}")
            subprocess.run(['kubectl', 'scale', 'deployment', '-n', namespace, name, f'--replicas={scale}'])
            return replicas

def get_feeds_db_sts(namespace):
    try:
        result = subprocess.run(['kubectl', 'get', 'sts', '-n', namespace], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')[1:]
        stateful_sets = [line.split()[0] for line in lines]
        for sts in stateful_sets:
            if "enterprise-feeds-db" in sts:
                return sts.split()[0]
    except subprocess.CalledProcessError:
        print(f"Error: Unable to list sts in the '{namespace}' namespace.")
        exit(2)

def wait_for_connections(namespace, statefulset):
    print("Waiting for database connections to drop...")
    for i in range(1, 60):
        print(f" - Attempt {i}: {statefulset} database", end='')
        try:
            command = ['kubectl', 'exec', '-it', f'statefulset.app/{statefulset}', '-n', namespace, '--', 'sh', '-c', f'PGPASSWORD="$POSTGRES_PASSWORD" psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -X -A -w -t -c "SELECT count(*) FROM pg_stat_activity;"']
            result = subprocess.run(command, capture_output=True, text=True)
            output = int(result.stdout.strip())
            if output > 1:
                print(f" - {output} connections remaining")
                time.sleep(5)
            else:
                print(" - done")
                break
        except subprocess.CalledProcessError:
            print(f"Error: Unable to connect to {statefulset}")
            exit(2)


def backup(namespace, databases, statefulset):
    print("Backing up databases...")
    for dep in databases:
        db = maindb_name if "postgres" in dep else feeddb_name
        filename = maindb if "postgres" in dep else feeddb
        print(f" - {dep} database is being dumped to {filename}")
        command = ['kubectl', 'exec', '-it', f'statefulset.app/{statefulset}', '-n', namespace, '--', 'sh', '-c', f'PGPASSWORD="$POSTGRES_POSTGRES_PASSWORD" pg_dump -U postgres -h localhost -C -c -d {db}']
        result = subprocess.run(command, capture_output=True, text=True)
        with open(filename, 'w') as f:
            f.write(result.stdout)
        print(result.stderr)

def restore(namespace, databases, statefulset):
    print("Restoring databases...")
    for dep in databases:
        filename = maindb if "postgres" in dep else feeddb
        print(f" - {dep} database is being restored from {filename}. Logs stored at {filename}.restore.log")
        subprocess.run(['kubectl', 'exec', '-it', f'statefulset.app/{statefulset}', '-n', namespace,
                        '--', 'sh', '-c', f'PGPASSWORD="$POSTGRES_POSTGRES_PASSWORD" psql -h localhost -U postgres -d postgres'], stdin=open(filename, 'r'),
                       stdout=open(f'{filename}.restore.log', 'w'), stderr=subprocess.STDOUT)

def main():
    global maindb, feeddb, maindb_name, feeddb_name

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Anchore Database Backup and Restore")
    parser.add_argument('-b', action='store_const', const='backup', dest='action',
                        help="Perform a backup. This is the default.")
    parser.add_argument('-r', action='store_const', const='restore', dest='action',
                        help="Perform a restore.")
    parser.add_argument('-n', '--namespace', default='anchore',
                        help="The namespace Anchore is deployed in. Defaults to anchore.")
    # parser.add_argument('-m', '--maindb', help="The filename to backup/restore the main Anchore database.")
    parser.add_argument('-f', '--feeddb', help="The filename to backup/restore the Anchore feed database.")
    # parser.add_argument('-d', '--maindb-name', default='anchore',
    #                     help="The name of the main database. The default is 'anchore'. Only used during backup.")
    parser.add_argument('-e', '--feeddb-name', default='anchore-feeds',
                        help="The name of the feeds database. The default is 'anchore-feeds'. Only used during backup.")
    parser.add_argument('-c', '--clamav', action='store_const', const='clamav', dest='action',
                        help="Update or download the ClamAV Database")
    args = parser.parse_args()

    # No action specified
    if not args.action:
        print("Error: No valid action specified!\n\n")
        parser.print_usage()
        exit(1)

    if args.action == "clamav":
        check_config()
        show_config()
        update_database()
    else:

        feeddb, feeddb_name = args.feeddb, args.feeddb_name

        # Get the name of the database pods
        feeds_name = subprocess.run(['kubectl', 'get', 'deployment', '-n', args.namespace], capture_output=True, text=True)
        feeds_name = [line.split()[0] for line in feeds_name.stdout.strip().split('\n') if 'feeds' in line][0]

        # Determine which databases to use
        databases = []
        # if maindb:
        #     databases.append(main_name)
        if feeddb:
            databases.append(feeds_name)

        # No databases were specified, so let's bail
        if not databases:
            print("Error: No databases specified!\n\n")
            parser.print_usage()
            exit(1)

        # Get the deployments
        deployments = get_deployments(args.namespace)

        # Scale down the deployments
        feeds_replicas = scale(args.namespace, 'down', deployments, 0)
        print(f"Original Replicas: {feeds_replicas}")

        # Get Feeds STS
        feeds_sts = get_feeds_db_sts(args.namespace)
        print(f"Feeds STS: {feeds_sts}")

        # Wait for connections to the db's to drop
        wait_for_connections(args.namespace, feeds_sts)

        if args.action == "backup":
            backup(args.namespace, databases, feeds_sts)
        elif args.action == "restore":
            restore(args.namespace, databases, feeds_sts)   

        # Scale up the deployments
        scale(args.namespace, 'up', deployments, feeds_replicas)

        print("\nComplete! Please review the output files to ensure no errors were encountered during the backup/restore process.")

if __name__ == "__main__":
    main()
