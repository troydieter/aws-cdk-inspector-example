import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="cdk_inspector_poc",
    version="1.0.0",

    description="AWS Inspector CDK POC",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="odonoha@luxoft.com",
    package_dir={"": "cdk_inspector_poc"},
    packages=setuptools.find_packages(where="cdk_inspector_poc"),

    install_requires=[
        "aws-cdk-lib>=2.0.0",
        "constructs>=10.0.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
