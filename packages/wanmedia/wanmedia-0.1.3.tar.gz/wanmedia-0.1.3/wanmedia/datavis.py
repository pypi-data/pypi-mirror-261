from wordcloud import WordCloud
import pyLDAvis
from pyLDAvis import gensim_models


def LDA_graph(model,work_frequency,dictionary, notebook_enable=True):
    if notebook_enable==True:
        pyLDAvis.enable_notebook()
    return gensim_models.prepare(model,words_frequency,dictionary=dictionary)