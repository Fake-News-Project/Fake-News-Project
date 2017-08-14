#  Identifying Fake News


## Project Description

The increased use of the Internet or social medias to share news has allowed information to travel at record speeds. However, it has also led to the rise of fake news stories, a recent phenomenon that relies on the ability of an article to go "viral" without being vetted by an editorial team, as in traditional news sources. This project seeks to identify fake or highly-biased news articles to help prevent the spread of false information. More specially, we implemented a program to examine the existence of authors, words and punctuation usage in titles, and article bodies, and used machine learning algorithms to identify news from unreliable sources. 


## Building Dataset 
Our final dataset (**_balanced_data.csv_** under data directory) contains 1473 articles from reliable sources and 1473 from unreliable sources. Items from reliable sources have attribute _authenticity_ as 0, while entities from ureliable sources have _authenticity_ of 1. 

#### 1. Collect Data
Our data collection scripts:

* _Step1_CollectData_Hyesoo.ipynb_ (Hyesoo's script)
* _Step1_CollectData_Jinmei_FakeNews.ipynb_ and _Step1_CollectData_Jinmei_RealNews.ipynb_ (Jinmei's script')

used the Python library [***Newspaper***](http://newspaper.readthedocs.io/en/latest/) that collects information of articles from a wide variety of news sources. 

We have collected news from 12 reliable news sources and 42 unreliable news websites. 
* The reliable sources include **_msnbc_**, **_nbcnews_**, **_politico_**, **_foxnews_**, **_nytimes_**, **_reuters_**, **_abc_**, **_bbc_**, **_cnn_**, **_newyorker_**, **_cbsnews_**, and **_npr_**.
* The unreliable news sources we used are
**_24wpn_**, **_beforeitsnews_**, **_readconservatives_**, **_newsbbc_**, **_now8news_**, **_americanfreepress_**, **_nephef_**, **_nationonenews_**, **_infostormer_**, **_Conservativedailypost_**, **_donaldtrumppotus45_**, **_ladylibertysnews_**, **_interestingdailynews_**, **_president45donaldtrump_**, **_openmagazines_**, **_krbcnews_**, **_bizstandardnews_**, **_bipartisanreport_**, **_local31news_**, **_nbcnews_**, **_CivicTribune_**, **_politicono_**, **_redcountry_**, **_AmericanFlavor_**, **_ddsnewstrend_**, **_Clashdaily_**, **_realnewsrightnow_**, **_wordpress_**, **_reagancoalition_**, **_lastdeplorables_**, **_Americannews_**, **_aurora-news_**, **_thedcgazette_**, **_politicalo_**, **_newswithviews_**, **_pamelageller_**, **_Bighairynews_**, **_ABCnews_**, **_sputniknews_**, **_prntly_**, **_Americanoverlook_**, and **_majorthoughts_**.

#### 2. Clean Data

Data collected with _Step1_CollectData_Hyesoo.ipynb_ use the script, _Step2_CleanData_Hyesoo.ipynb_, to remove short articles and errors.

#### 3. Merge Data

Data collected by Hyesoo and Jinmei are merged with the script, _Step3_MergeData.ipynb_. It also includes cleaning procedure for data collected by Jinmei.


## Feature engineering

Features include
* existence of authors
* exaggerating punctuations used in titles
* rate of uppercases used in titles
* TF-IDF values generated with text body

The first three features were generated using _Step4_GenerateExtraFeatures.ipynb_ script. They were rescaled with TF-IDF features afterwards.


## Predicting fake news with various machine learning classifiers 
Models used include

* Naive Bayes
* Logistic Regression
* Neural Network (MLPclassifier)
* Random Forest
* Support Vector Machine

See script _Step5_ExtractFeatures_Predict_w_MachineLearning.ipynb_ for details.
## Results
We are able to obtain > 92 % prediction accuracy within our dataset.


## References 
Lists of fake news websites:
* https://github.com/BigMcLargeHuge/opensources
* http://www.fakenewsai.com/
* https://mediabiasfactcheck.com/fake-news/
