from setuptools import setup, find_packages

setup(
    name='lucy-spc',
    version='0.0.1',
    author='Aswin Venkat',
    author_email='aswinvenkat60@gmail.com',
    description='A Python library for reading and writing .spc files',
    long_description=open('README.md').read() + "\n\n" + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aswin-kevin/lucy-spc',
    packages=find_packages(),
    install_requires=[],
    license="MIT",
    keywords="spc",
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
)
