from setuptools import setup

setup(
    name='wanmedia',
    version='0.1.0',
    description='Social Media  Analysis ',
    packages=['wanmedia'],
    install_requires=[
        'nltk',
        'stop_words',
        'hdbscan',
        'top2vec',
        'top2vec[sentence_encoders]',
        'tmplot'


    ]
)
