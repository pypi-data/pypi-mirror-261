from setuptools import setup, find_packages

setup(
    name="chartscraper",
    version="0.1",
    author="Aniket Inamdar",
    author_email="aniketinamdar02@gmail.com",
    description="Python module that scrapes tradingview charts when appropriate inputs are given.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click","selenium"],
    entry_points={"console_scripts": ["chart-scrapper = chartscrapper:get_chart"]},
)