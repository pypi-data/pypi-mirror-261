from setuptools import setup

setup(
    name="leaping",
    version="0.1.4",
    entry_points={
        'console_scripts': [
            'leaping=leaping:main',
        ],
    },
    install_requires=[
        "pytest-leaping==0.1.3",
    ],
)
