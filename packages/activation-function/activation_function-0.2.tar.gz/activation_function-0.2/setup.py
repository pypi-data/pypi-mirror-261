from setuptools import setup, find_packages

setup(
    name='activation_function',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'kivy',  # Add 'kivy' as the graphics library
    ],
)
