from flask import Flask
from flask import request
from flask import render_template
from compute_score import compute_score

app = Flask(__name__)

@app.route('/')
def my_form():
  return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

  url = request.form['url']
  # function to compute the score for the probability of being fake news
  # processed_text = url.upper()
  test = compute_score(str(url))
  return test

if __name__ == '__main__':
  app.run()
