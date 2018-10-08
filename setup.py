from setuptools import find_packages, setup

setup(
    name="django-coffeeapp-backend",
    packages=find_packages(),
    include_package_data=True,
    description="The backend for Coffee Project's mobile app.",
    install_requires=["django >= 2.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
