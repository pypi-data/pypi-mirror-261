from setuptools import setup, find_packages

setup(         
    name='activationFunctionVisualizer',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        # 'kivy',  # Add 'kivy' as the graphics library
    ],
)
