import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import validation_curve
from sklearn.metrics import f1_score

import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize_stemmer(text):
    tokens = nltk.word_tokenize(text)
    # option to include punctuation or not
    #tokens = [i for i in tokens if i not in string.punctuation]
    stems = stem_tokens(tokens, stemmer)
    return stems

def valid_test(model, param, param_candidates, x_cv_dtm, y_cv):
    train_scores, valid_scores = validation_curve(model, x_cv_dtm, y_cv, param, param_candidates)
    avg_ts, avg_vs = train_scores.mean(axis=1), valid_scores.mean(axis=1)
    sd_ts, sd_vs = train_scores.std(axis=1), valid_scores.std(axis=1)
    vs_max_ix = np.argmax(avg_vs)
    best = param_candidates[vs_max_ix]
    print('The best {} value for {} is {}'.format(param, model, best))
    return best

def print_scores(model, x_train_dtm, y_train, x_test_dtm, y_test, y_test_pred):
    print('Train score is {}'.format(model.score(x_train_dtm, y_train)))
    print('Test score is {}'.format(model.score(x_test_dtm, y_test)))
    print('F1 score is {}'.format(f1_score(y_test, y_test_pred)))

def compute_score(url):
    # import data
    path = os.path.join('data', 'balanced_data.csv')
    total_df = pd.read_csv(path, usecols=[1, 2, 3, 5, 6])

    fake_websites = list(set(list(total_df['source'][total_df.authenticity == 1])))
    true_websites = list(set(list(total_df['source'][total_df.authenticity == 0])))
    print("The number of total real news websites scraped is {} and that of fake ones is {}"
          .format(len(true_websites), len(fake_websites)))

    # Define training, cross-validation and testing sets
    Y = total_df['authenticity']
    X = total_df.text

    X_train, X_cvt, Y_train, Y_cvt = train_test_split(X, Y, test_size=0.3, random_state=42)
    X_cv, X_test, Y_cv, Y_test = train_test_split(X_cvt, Y_cvt, test_size=0.6, random_state=42)

    print("Shape of X_train is {}, X_cv is {}, X_test is {}"
          .format(X_train.shape, X_cv.shape, X_test.shape))

    # obtain new articles
    # obtain a article and parse it
    from newspaper import Article
    #url = 'http://www.cnn.com/2017/07/18/politics/obamacare-fail-trump/index.html'
    article = Article(url)
    article.download()
    article.parse()
    print(article.title)
    print(article.authors)
    print(article.publish_date)
    X_test = [article.text]

    # use TF-IDF to generate features for the text body of news
    my_additional_stop_words = ['abc', 'nbc', 'npr', 'cnn', 'reuters', 'fox',
                                'bbc', 'cbs', 'newyorker', 'msnbc', 'politico', 'nytimes',
                                'sputniknews', 'lastdeplorables', 'readconservatives', 'wordpress',
                                'infostormer', 'Americannews', 'ABCnews', 'nationonenews', 'majorthoughts',
                                'interestingdailynews', 'donaldtrumppotus45', 'newsbbc', 'beforeitsnews',
                                'krbcnews', 'Conservativedailypost', 'thedcgazette', 'Americanoverlook',
                                'CivicTribune', 'openmagazines', 'politicono', 'bizstandardnews',
                                'president45donaldtrump',
                                'nbc', 'AmericanFlavor', 'prntly', 'bipartisanreport', 'americanfreepress',
                                'ladylibertysnews', 'politicalo', 'now8news', '24wpn', 'pamelageller',
                                'ddsnewstrend', 'Bighairynews', 'redcountry', 'newswithviews', 'Clashdaily',
                                'aurora-news', 'nephef', 'local31news', 'realnewsrightnow', 'reagancoalition',
                                'reuter', 'sputnik',
                                'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    my_stop_words = text.ENGLISH_STOP_WORDS.union(my_additional_stop_words)
    # tfidf = TfidfVectorizer(tokenizer=tokenize_stemmer,stop_words=my_stop_words,ngram_range=(1, 2))
    tfidf = TfidfVectorizer(tokenizer=tokenize_stemmer, stop_words='english', ngram_range=(2, 2))
    tfidf.fit(X_train)

    X_train_tot = tfidf.transform(X_train)
    print("X_train_tot shape: ", X_train_tot.shape)

    X_test_tot = tfidf.transform(X_test)
    X_cv_tot = tfidf.transform(X_cv)

    # feature selection from model
    lsvc = LinearSVC(C=9000, penalty="l1", dual=False)
    selector = SelectFromModel(lsvc, prefit=False)
    selector.fit(X_train_tot, Y_train)
    X_train_selected = selector.transform(X_train_tot)

    X_test_selected = selector.transform(X_test_tot)
    X_cv_selected = selector.transform(X_cv_tot)

    print("X_train_selected shape: ", X_train_selected.shape)
    print("X_test_selected shape: ", X_test_selected.shape)
    print("X_cv_selected shape: ", X_cv_selected.shape)

    X_train_dtm = X_train_selected
    X_test_dtm = X_test_selected
    X_cv_dtm = X_cv_selected

    # Prediction
    best_C = valid_test(LogisticRegression(), "C", np.logspace(2, 4, 10), X_cv_dtm, Y_cv)
    LR = LogisticRegression(C=best_C)

    LR.fit(X_train_dtm, Y_train)
    Y_test_pred_LR = LR.predict(X_test_dtm)

    print("Y_test_pred_LR: ", Y_test_pred_LR[0])

    if Y_test_pred_LR[0] == 0:
        return "This is a true news article"
    else:
        return "This is a fake news article"

def compute_score_test(url):
    print(url)
    Y = 0
    if Y == 0:
        return "this is true"
    else:
        return "this is fake"
#url = 'http://www.cnn.com/2017/07/18/politics/obamacare-fail-trump/index.html'
#compute_score(url)