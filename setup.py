from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_resource/__init__.py
from frappe_resource import __version__ as version

setup(
	name="frappe_resource",
	version=version,
	description="Frappe Code Snippets",
	author="Rowena",
	author_email="sabellita.ro@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
