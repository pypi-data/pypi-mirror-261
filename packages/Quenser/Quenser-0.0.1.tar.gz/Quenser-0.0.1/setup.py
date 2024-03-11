from setuptools import setup, find_packages

setup(
    name="Quenser",
    version="0.0.1",
    author="Tassana Khrueawan",
    author_email="tassana.khr@gmail.com",
    description="Hello world Testing Library for Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tassh571/Quenser.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
