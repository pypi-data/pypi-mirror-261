import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ni_card_controller",
    version="0.0.2",
    author="Anibal Gatica",
    author_email="anibal.gatica@domin.co",
    description="A package to control NI cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Domin-co/ni-card-controller",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["numpy", "pandas", "matplotlib", "redis", "pydantic", "nidaqmx"],
    extras_require={
        "dev": ["check-manifest"],
    },
)
