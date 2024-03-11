from setuptools import setup

setup(
    name='wanmedia',
    version='0.2.2',
    description='Social Media  Analysis ',
    packages=['wanmedia'],
    install_requires=[
        'nltk',
        'stop_words',
        'hdbscan',
        'top2vec',
        'top2vec[sentence_encoders]',
        'tmplot',
        'gensim',
        'pyLDAvis'

    ]
)
