from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='codeatics',
    version='0.1.0',
    author='PrabhuBikash😎',
    description='A collection of useful stuff',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PrabhuBikash/codeatics',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[],
    python_requires='>=3.6',
)