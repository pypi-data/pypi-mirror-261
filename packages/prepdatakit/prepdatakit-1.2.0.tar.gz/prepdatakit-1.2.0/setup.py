from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='prepdatakit',
    version='1.2.0',
    author='Abdulaziz Yabrak',
    author_email='abdulaziz.mofid@gmail.com',
    description='A Python toolkit for preprocessing datasets.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
