#  Identifying Fake News

## Project Description

As fake news is becoming more and more common on the internet, the risk of false stories spreading has increased. However, by looking at the difference in language between more reputable sites and fake news sites it may be possible to flag fake articles. This challenge includes scraping articles, engineering features, and developing a model to classify articles as fake news or reputable.



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
