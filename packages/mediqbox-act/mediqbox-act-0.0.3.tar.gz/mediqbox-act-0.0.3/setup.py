from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fp:
  long_description = fp.read()

setup(
  name="mediqbox-act",
  version="0.0.3",
  description="A mediqbox component for translating texts and files",
  long_description=long_description,
  long_description_content_type="text/markdown",
  package_dir={"": "src"},
  packages=find_namespace_packages(
    where="src", include=["mediqbox.*"]
  ),
  install_requires=[
    "mediqbox-download",
    "requests-toolbelt"
  ]
)