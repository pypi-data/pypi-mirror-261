from setuptools import setup, find_packages

setup(
    name='pixegami',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.11.1'
    ],
    entry_points={
        "console_scripts": [
            "pixegami-hello = pixegami:hello",
        ],
    }
)