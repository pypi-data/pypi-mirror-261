import setuptools

requirements = ["httpx"]

setuptools.setup(
    name="AminoZ",
    version="0.0.1",
    author="ZOOM",
    author_email="hgdcytdgh@gmail.com",
    description="Amino App Library",
    long_description="README.md",  # يفضل تحديد محتوى README.md الذي يشمل وصفًا طويلاً للمشروع.
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    python_requires=">=3.6",
)

