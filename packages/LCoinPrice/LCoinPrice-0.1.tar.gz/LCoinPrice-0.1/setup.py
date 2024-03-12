from setuptools import setup, find_packages

with open("README.md", "r") as f:
  description= f.read()
setup(
  name="LCoinPrice",
  version="0.1",
  install_requires=[
    "pycoingecko",
  ],
  long_description=description,
  long_description_content_type="text/markdown"
)