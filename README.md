#  Identifying Fake News


## Project Description

The increased use of the Internet or social medias to share news has allowed information to travel at record speeds. However, it has also led to the rise of fake news stories, a recent phenomenon that relies on the ability of an article to go "viral" without being vetted by an editorial team, as in traditional news sources. This project seeks to identify fake or highly-biased news articles and thus prevent the spread of false information. As such, we have developed a model that classifies articles as real and trusted, verses fake and highly-biased. To determine the authenticity of each article, we examine the existence of authors, various words or punctuation usage in the title the an article body, and so on. By flagging fake or highly-biased news articles, we hope to reduce their spreading. 


## Building data 

To gather a dataset, we wrote a web-scraper using python opensource ***Newspaper***(http://newspaper.readthedocs.io/en/latest/) that downloads articles from a wide variety of news sources. 
* The number of total real news websites scraped is 42 and that of fake ones is 12.

* Real news websites scraped are:
['msnbc', 'nbcnews', 'politico', 'foxnews', 'nytimes', 'reuters', 'abc', 'bbc', 'cnn', 'newyorker', 'cbsnews', 'npr']

* Fake news websites scraped are:
['24wpn', 'beforeitsnews', 'readconservatives', 'newsbbc', 'now8news', 'americanfreepress', 'nephef', 'nationonenews', 'infostormer', 'Conservativedailypost', 'donaldtrumppotus45', 'ladylibertysnews', 'interestingdailynews', 'president45donaldtrump', 'openmagazines', 'krbcnews', 'bizstandardnews', 'bipartisanreport', 'local31news', 'nbcnews', 'CivicTribune', 'politicono', 'redcountry', 'AmericanFlavor', 'ddsnewstrend', 'Clashdaily', 'realnewsrightnow', 'wordpress', 'reagancoalition', 'lastdeplorables', 'Americannews', 'aurora-news', 'thedcgazette', 'politicalo', 'newswithviews', 'pamelageller', 'Bighairynews', 'ABCnews', 'sputniknews', 'prntly', 'Americanoverlook', 'majorthoughts']

* After cleaning and balancing the data, we had 1473 articles for each category.


## Feature engineering

#### Features generated:
* Existence of authors
* Exaggerating punctuations used in title
* Rate of uppercases used in title
* TF-IDF features on article body text

#### Features were selected and scaled after generated


## Prediction using various machine learning classifiers 
(scikit-learn libraries in python)

* Logistic regression
* Neural network (MLPclassifier)
* Naive Bayes
* Random Forest
* SVM


## References 

* http://newspaper.readthedocs.io/en/latest/
* https://github.com/BigMcLargeHuge/opensources
* http://www.fakenewsai.com/
* https://mediabiasfactcheck.com/fake-news/
