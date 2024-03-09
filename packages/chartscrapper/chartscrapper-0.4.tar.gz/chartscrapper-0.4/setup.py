from setuptools import setup, find_packages

setup(
    name='chartscrapper',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'selenium'
    ],
    entry_points={
        "console_scripts":[
            "chart-scrapper = chartscrapper:get_chart",
        ],
    },
)
