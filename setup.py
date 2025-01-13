from setuptools import find_packages, setup

setup(
    name="netbox-oxidized",
    version="1.0.0",
    description="A NetBox plugin for displaying Oxidized backups.",
    author="sz",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    entry_points={
        "netbox_plugins": [
            "netbox_oxidized = netbox_oxidized"
        ]
    },
)