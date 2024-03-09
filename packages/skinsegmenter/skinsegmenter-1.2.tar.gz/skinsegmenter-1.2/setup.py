from setuptools import setup, find_packages


with open("README.md") as f:
    description = f.read()

setup(
    name="skinsegmenter",
    version="1.2",
    packages=find_packages(),
    install_requires=[
        "ultralytics",
        "gdown"
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)