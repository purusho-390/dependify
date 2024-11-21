from setuptools import setup, find_packages

setup(
    name="dependify",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Add core dependencies if needed
    entry_points={
        "console_scripts": [
            "dependify=dependify.main:main",
        ],
    },
    description="A tool to auto-detect and install missing Python dependencies.",
    author="Purushothaman M",
    url="https://github.com/yourusername/dependify",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
