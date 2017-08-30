from flask import Flask
from flask import request
from flask import render_template
import check_an_article
# from check_an_article import check_authenticity, concat_3features
# import pandas as pd
# import numpy as np
# import scipy as sp
# from flask import render_template
# import dill as pickle
# import string
# from nltk.stem.porter import PorterStemmer
# from nltk import word_tokenize




app = Flask(__name__)

@app.route('/')
def index():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def index2():
    if check_an_article.check_authenticity(str(request.form['url'])) > 0.5:
        return render_template("fake.html")
    else:
        return render_template("real.html")

if __name__ == '__main__':
  app.run()
