from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='neodb',
    version='0.0.1',
    description="a simple tool to monitor execution times of functions.",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    py_modules=['InMemoryBackend'],
    url='https://github.com/eyukselen/bumi',
    license='MIT',
    author='emre',
    author_email='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    project_urls={
        'Homepage': 'https://github.com/eyukselen/bumi',
        'Source': 'https://github.com/eyukselen/bumi',
    }
)
