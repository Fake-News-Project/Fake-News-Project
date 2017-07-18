#  Identifying Fake News 

## Project Description 

As fake news is becoming more and more common on the internet, the risk of false stories spreading has increased. However, by looking at the difference in language between more reputable sites and fake news sites it may be possible to flag fake articles. This challenge includes scraping articles, engineering features, and developing a model to classify articles as fake news or reputable.

## Inputs and Outputs 
### Inputs
possible options: article title, url, tweet, ....

### Outputs
fake news or not

## Design

### Possible ways to detect fake news:

#### Source 
* url that ends with lo or com.co
* website does not have “About Us” tab or it sounds suspicious

#### Lack of author 

#### Headline
* whether similar headlines exist

#### Text (article body)
* all caps
* hyperbolic words
* sensational or provocative language

#### Citation frequency (number of responses) on Facebook/Twitter


### Proposals by Hyesoo
* focus on political news
* focus on Twitter news

## Reference
[On The Media Fake News Handbook]("http://www.wnyc.org/story/breaking-news-consumer-handbook-fake-news-edition/")
