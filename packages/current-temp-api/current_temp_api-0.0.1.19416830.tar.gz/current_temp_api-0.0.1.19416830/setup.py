import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="current_temp_api",
    version="0.0.1.0019416830",
    author="Hossein AmirAbdollahi",
    author_email="HosseinAmirAbdollahi8@gmail.com",
    description="a simple client API module to get current temperature from service providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hossein-amirabdollahi/Python-Current-Temperature-API",
    project_urls={
        "Author": "https://www.linkedin.com/in/hossein-amirabdollahi-6070b7294/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
