import setuptools

requirements = ["httpx"]


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="AminoZ",
    version="0.1.0",
    author="ZOOM",
    author_email="hgdcytdgh@gmail.com",
    description="Amino App Library",
    long_description=long_description,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    python_requires=">=3.6",
)

