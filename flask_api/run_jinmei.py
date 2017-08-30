from flask import Flask
from flask import request
from flask import render_template
from compute_score import compute_score

app = Flask(__name__)

@app.route('/')
def my_form():
  return render_template("get-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

  url = request.form['url']
  # function to tell whether the url gives a fake or real news
  result = compute_score(url)
  return render_template("post-form.html", result=result)

if __name__ == '__main__':
  app.run()
