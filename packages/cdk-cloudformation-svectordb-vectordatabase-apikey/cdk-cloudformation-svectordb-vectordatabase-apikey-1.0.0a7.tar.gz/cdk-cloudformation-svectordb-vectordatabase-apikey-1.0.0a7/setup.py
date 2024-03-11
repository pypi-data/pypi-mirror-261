import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-cloudformation-svectordb-vectordatabase-apikey",
    "version": "1.0.0.a7",
    "description": "Generates an API key to access a SvectorDB serverless vector database, sign up at https://svectordb.com to get started",
    "license": "Apache-2.0",
    "url": "https://github.com/cdklabs/cdk-cloudformation.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/cdk-cloudformation.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_cloudformation_svectordb_vectordatabase_apikey",
        "cdk_cloudformation_svectordb_vectordatabase_apikey._jsii"
    ],
    "package_data": {
        "cdk_cloudformation_svectordb_vectordatabase_apikey._jsii": [
            "svectordb-vectordatabase-apikey@1.0.0-alpha.7.jsii.tgz"
        ],
        "cdk_cloudformation_svectordb_vectordatabase_apikey": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.132.0, <3.0.0",
        "constructs>=10.3.0, <11.0.0",
        "jsii>=1.95.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
