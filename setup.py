from setuptools import setup, find_packages

setup(
    name='zendesk-ticket-insights',
    version='0.1.0',
    description='A data science project for EDA and sentiment analysis of Zendesk tickets.',
    author='Yew Zi Huang',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn'
    ],
)
