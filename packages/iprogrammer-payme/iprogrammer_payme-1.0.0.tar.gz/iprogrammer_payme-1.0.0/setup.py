import setuptools

setuptools.setup(
    name="iprogrammer_payme",
    version="1.0.0",
    author="A'zamov Samandar",
    author_email="azamov.samandar.programmer@gmail.com",
    description="IProgrammer Payme",
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests', 'django', 'djangorestframework'],
    url="https://github.com/ExcelentProgrammer/iprogrammer_payme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
