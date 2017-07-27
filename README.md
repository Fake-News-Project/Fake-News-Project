#  Identifying Fake News

## Project Description

The increased use of the Internet to share news has allowed information to travel at record speeds. However, it has also led to the rise of fake news stories, a recent phenomenon that relies on the ability of an article to go "viral" without being vetted by an editorial team, as in traditional news sources. This project seeks to identify unreputable news sources and thus prevent the spread of false information. As such, we have developed a model that classifies articles as reputable or not reputable. We examine the structure of the articles, including length, variety of word choice, and use of standard grammar, to determine the likelihood of being reputable or non-reputable. By flagging non-reputable sources, we hope to reduce the spread of highly biased or fabricated news. 

## Data ## 

To gather a high quality dataset, we wrote a scraper that downloads articles from a wide variety of news sources. Each team member (3) downloaded a set of articles from reputable and non-reputable news sources. The binary categorization for the news sources 

-logistic regression
-enural nets
-library for unexpected
-naive bayes 

-6000 data
-1500 as cross validation 
## Model ## 

Machine Learning Model (Unspervised, Supervised Learning Model) 

## References ## 



## Inputs and Outputs
* ### Inputs
url of the article <br />
(alternative option: article title)

* ### Outputs
Binary decision (fake or not)



## Dataset (on debate)

* A dataset published by Signal Media
(http://research.signalmedia.co/newsir16/signal-dataset.html")

* Alternatively, we could web-scrap the articles by ourselves

* Determining 'Fake or not' of the training dataset: <br />
Use OpenSources.co to distinguish between 'legitimate' and 'fake' news sources

## Day 2 Discussion ##

-word frequency
-length
-grammar
-bias vs fake
-manual/ human moderators
-probability of fake (already in outcome)
-cross validating

-satirical comedy – exclude the onion 
-download dataset separately

## Design
#### Source
* Considered mistrustful from the general audience
* url that ends unusually (eg. lo, to, com.co )
* Website does not have “About Us” tab
* Lack of author
* author verified (blue arrow on FB and twitter) 


#### Writing style
* Following AP Style Guide?
* all caps
* hyperbolic words
* sensational or provocative language
* considerably low number of 'unique' words used (may reflect the low quality of the article)

#### Social media analysis
* Citation frequency (number of responses) on Facebook/Twitter (in case the news organization is fishy, but the article is viral)

#### More ideas
* focus on political news only, in case we decide to web-scrap the articles


## Reference
[On The Media Fake News Handbook]("http://www.wnyc.org/story/breaking-news-consumer-handbook-fake-news-edition/") <br />
[Opensources]("http://www.opensources.co/") <br />
https://github.com/aldengolab/fake-news-detection
