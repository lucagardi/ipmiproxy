"""Setup script for ipmiproxy."""
from setuptools import setup, find_packages

setup(
    name='ipmiproxy',
    version='21.12.1',
    description="Python wrapper around ipmitool",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    keywords='ipmi cipher security lanplus',
    url='https://gitlab.cern.ch/hw/ipmiproxy',
    author='Luca Gardi',
    author_email='luca.gardi@cern.ch',
    maintainer='CERN IT Procurement',
    maintainer_email='procurement-team@cern.ch',
    license='GPL',
    scripts=['bin/ipmiproxy'],
)
