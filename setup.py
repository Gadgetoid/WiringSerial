#!/usr/bin/env python

from setuptools import setup, find_packages, Extension
from glob import glob

_wiringserial = Extension(
		'_wiringserial',
		include_dirs=['.'],
		sources=glob('*.c')
		)

setup(
		name = 'wiringserial',
		version = '0.0.1',
		author = "Philip Howard",
		author_email = "phil@gadgetoid.com",
		url = 'https://github.com/Gadgetoid/WiringSerial/',
		description = "",
		long_description="",
		ext_modules = [ _wiringserial ],
		py_modules = ["wiringserial"],
		install_requires=[],
		headers=glob('*.h')
		)
