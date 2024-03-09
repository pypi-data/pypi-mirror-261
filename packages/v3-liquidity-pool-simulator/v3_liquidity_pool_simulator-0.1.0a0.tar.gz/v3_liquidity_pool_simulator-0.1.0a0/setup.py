from setuptools import setup, find_packages


setup(
    name="v3_liquidity_pool_simulator",
    version="0.1.0-alpha",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple simulator for Uniswap V3 liquidity pools.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/v3_liquidity_pool_simulator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
    install_requires=open('requirements.txt').read().splitlines(),
)
