import setuptools


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setuptools.setup(
    name="tsp-art",
    version="1.0.0",
    description="Construct and solve TSP instances generated from images.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='optimization tsp art image',
    url="https://github.com/andremaravilha/tsp-art",
    author="Andre L. Maravilha",
    author_email="andre.maravilha@outlook.com",
    license='MIT',
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'Pillow',
        'numpy',
        'scipy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': ['tsp-art=tspart.__main__:main']
    },
    include_package_data=True,
    zip_safe=False
)
