import pandas as pd
import numpy as np
import scipy as sp
from flask import render_template
import dill as pickle
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from newspaper import Article
from sklearn.feature_extraction.text import TfidfVectorizer


def stem_tokens(tokens, stemmer):
    stemmer = PorterStemmer()
    return [stemmer.stem(x) for x in tokens]

def tokenize_stemmer(text):
    tokens = word_tokenize(text)
    return stem_tokens(tokens, stemmer)

LR = pickle.load(open('LR.sav', 'rb'))
tfidf = pickle.load(open('tfidf.sav', 'rb'))
selector = pickle.load(open('selector.sav', 'rb'))


def concat_3features(df):
    author = np.array([[x] for x in df.author])
    caprate = np.array([[x] for x in df.caprate_title])
    exagg =  np.array([[x] for x in df.exagg_puct_title])
    return  np.concatenate((author, caprate, exagg), axis=1)

def check_authenticity(url):
    article = Article(url)
    article.download()
    article.parse()
    df = pd.DataFrame(index = ['article'], columns =['title', 'author', 'text'])
    df.text[0], df.author[0], df.title[0] = article.text, article.authors, article.title

    df.author[df.author == '[]'] = 0
    df.author[df.author != 0]  = 1
    title_list= list(df.title[0])
    num_cap_title = len([a for a in title_list if a.isupper()])
    len_title = df.title.str.len()
    df['caprate_title'] = num_cap_title/len_title
    df.caprate_title /= 0.9999999999999966

    num_exag_title = len([a for a in title_list if (a == ('!' or '?' or ':' or '-'))])
    df['exagg_puct_title'] = num_exag_title/len_title
    df.exagg_puct_title /= 1.0000000000000004

    X_test_tot = tfidf.transform([df.text[0]])
    X_test_selected = selector.transform(X_test_tot)
    X_test_sel_add = sp.sparse.hstack((X_test_selected, concat_3features(df[['author','caprate_title', 'exagg_puct_title']])))
    return LR.predict(X_test_sel_add)[0]
