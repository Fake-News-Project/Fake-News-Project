import pandas as pd
import numpy as np
import scipy as sp
from flask import render_template
import dill as pickle
import string
from nltk import word_tokenize, PorterStemmer
from newspaper import Article
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


def stem_tokens(tokens, stemmer):
    stemmer = PorterStemmer()
    return [stemmer.stem(x) for x in tokens]


def tokenize_stemmer(text):
    tokens = word_tokenize(text)
    # option to include punctuation or not
    #tokens = [i for i in tokens if i not in string.punctuation]
    stems = stem_tokens(tokens, stemmer)
    return stems

# stem_tokens = pickle.load(open('stem_tokens.pkl', 'rb'))
# tokenize_stemmer = pickle.load(open('tokenize_stemmer.pkl', 'rb'))
LR = pickle.load(open('LR.sav', 'rb'))
selector = pickle.load(open('selector.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))


def concat_3features(df):
    author = np.array([[x] for x in df.author])
    caprate = np.array([[x] for x in df.caprate_title])
    exagg =  np.array([[x] for x in df.exagg_puct_title])
    return  np.concatenate((author, caprate, exagg), axis=1)

def check_authenticity(url):
    article = Article(url)
    article.download()
    article.parse()
    df = pd.DataFrame(columns =['title', 'author', 'text'])
    df.text, df.author, df.title = article.text, article.authors, article.title

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
    print(df)
    tfidf_transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(vocabulary=pickle.load(open("vocab.pkl", "rb")))
    X_test_tot = tfidf_transformer.fit_transform(loaded_vec.transform(df.text))
    print ("a", X_test_tot.shape)
    X_test_selected = selector.transform(X_test_tot)
    print ("b", X_test_selected.shape)
    X_test_sel_add = sp.sparse.hstack((X_test_selected, concat_3features(df[['author','caprate_title', 'exagg_puct_title']])))
    print("c", X_test_sel_add.shape)
    test = scaler.transform(X_test_sel_add)
    print("d", test.shape)
    return LR.predict(test)
