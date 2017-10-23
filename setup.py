# Copyright (c) Microsoft Corporation. All Rights Reserved.
# Licensed under the MIT license. See LICENSE file on the project webpage for details.

"""Setup for azure_media_services XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, __, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='circle-ci',
    version='0.0.1',
    description='Description',
    packages=[
        'python_package',
    ],
    install_requires=[
        'PyJWT',
        'bleach',
        'mako',
        'XBlock',
        'xblock-utils==1.0.5',
    ],
    dependency_links=[
        'git+https://github.com/edx/xblock-utils.git@v1.0.3#egg=xblock-utils-1.0.5',
    ],
    entry_points={
        'xblock.v1': [
            'azure_media_services = azure_media_services:AMSXBlock',
        ]
    },
    package_data=package_data("azure_media_services", []),
)
