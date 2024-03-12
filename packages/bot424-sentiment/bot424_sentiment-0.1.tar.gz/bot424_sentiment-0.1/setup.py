from setuptools import setup, find_packages

setup(
    name='bot424_sentiment',
    version='0.1',
    packages=find_packages(),
    install_requires=['tweepy', 'textblob'],
    description='Fetches tweets and performs sentiment analysis',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
)