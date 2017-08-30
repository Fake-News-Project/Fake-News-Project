from flask import Flask
from flask import request
from flask import render_template
import check_an_article_final
import nltk
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    return [stemmer.stem(x) for x in tokens]

def tokenize_stemmer(text):
    tokens = word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def index2():
    if check_an_article_final.check_authenticity(request.form['url']) > 0.5:
        return render_template("fake.html")
    else:
        return render_template("real.html")

if __name__ == '__main__':
  app.run()
