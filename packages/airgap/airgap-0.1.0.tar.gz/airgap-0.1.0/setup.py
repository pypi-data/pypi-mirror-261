from setuptools import setup, find_packages

setup(
    name='airgap',
    version='0.1.0',
    packages=['airgap_sak'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "cvdupdate"
        # List your dependencies here

    ],
    entry_points={
        'console_scripts': [
            'airgap=airgap_sak.backup:main',
        ],
    },
)
