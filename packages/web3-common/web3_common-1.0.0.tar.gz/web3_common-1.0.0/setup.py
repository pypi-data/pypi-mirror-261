import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web3_common",
    version="1.0.0",
    author="yszr",
    author_email="yszr222@gmail.com",
    description="web3 commom utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(where='.', exclude=(), include=('*',)),
    package_data={"": ["*"]},
    include_package_data = True,
    classifiers=[
    ],
    python_requires='>=3.6',
    install_requires=[
        'web3==5.31.3',
    ],
    extras_require={":python_version=='3.6'": ["dataclasses==0.8"]}
)
