from setuptools import setup, find_packages

setup(
    name='passwordcrypto',
    version='1.0.0',
    packages=find_packages(),
    test_suite='tests',
    install_requires=[
        "cryptography"
    ],
    entry_points={
        'console_scripts': [
            # If your package provides command-line scripts, you can specify them here
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
)
