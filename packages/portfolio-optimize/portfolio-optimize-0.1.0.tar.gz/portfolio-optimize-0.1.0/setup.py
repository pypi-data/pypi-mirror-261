from setuptools import setup, find_packages

setup(
    name="portfolio-optimize",
    version="0.1.0",
    author="Manu Jayawardana",
    author_email="manujajayawardanais@gmail.com",
    description="Optimize stock portfolios using mean-variance optimization and other strategies.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/portfolio-optimize",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "yfinance", "matplotlib", "PyPortfolioOpt"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
