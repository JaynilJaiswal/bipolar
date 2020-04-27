# Bipolar news virality prediction

> It's a program to anticipate the virality of any news. I have created a database of ~53k news headlines which I have scraped. Using this database I predict the probability of headline going viral.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install below mentioned libraries:
```
Python >=v3.0
pip==20.0.2
beautifulsoup4==4.6.0
lxml==4.3.0
requests==2.21.0
nltk==3.5

```
### Installing

A step by step series of examples that tell you how to get a development env running

Create a virtual environment using python using:

```
python3 -m venv <myenvname>
```
Or you can just skip to installing the libraries:

```
pip install beautifulsoup4 lxml requests nltk
```

## Running the tests
To test the program, write the headline you wish to find viralty in file ```news_headline.txt```,then run the ``virality.py`` file.

### Method of virality calculation

Viralty of any news depends on the content of the news. Most of the important words are in the form of nouns. So I collect the nouns from the news headlines that I scraped and form an unigram based on count out of it. Using the unigram I find the individual probability of a noun going viral relative to the word most occured. The count of noun clearly indicates that it has appeared in many news headlines & hence is a trending topic.

Generally a news related to trending topics tend to go viral fast.
```
Probability of news having individual noun going viral = (Count_of_that_noun  - 1)/(The_max_count)
```
Suppose a noun appearing only 1 time then it's not likely to get viral, hence it's probability is zero while on the contrary the noun appearing maximum times is more likely to get viral.

### Method for scraping healines

Please refer to code of ``scrape.py`` file.
