from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='ud_util',
    version='0.1',
    author="Uday Dosajh",
    author_email="dosajhuday@gmail.com",
    description="sqlite utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages()
)
print(str(find_packages()))
print("process completed")
