from setuptools import find_packages, setup

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="inclusion",
    version="0.1.0",
    description="",
    author="Kay Kim",
    license="MIT license",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    setup_requires=[],
    install_requires=requirements,
    extras_require={},
    # entry_points={
    #     "console_scripts": [
    #         "manta=manta_client.cli.entry:cli",  # TODO: (kjw) need change
    #     ]
    # },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here.  # TODO: (kjw) need change
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    tests_require="",  # TODO: (kjw) need change
)
