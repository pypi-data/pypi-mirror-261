from setuptools import setup, find_packages
setup(
name='prepdatakit',
version='0.1.0',
author='Abdulaziz Yabrak',
author_email='abdulaziz.mofid@gmail.com',
description='A comprehensive toolkit for preprocessing datasets, including data reading, data summary generation, handling missing values, and categorical data encoding.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)