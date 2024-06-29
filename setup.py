from setuptools import setup, find_packages

setup(
    name="event-plugin-system",
    version="0.0.3",
    author="Carlos",
    author_email="chalonga@gmail.com",
    description="A simple plugin event system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chalonga/event-plugin-system",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
