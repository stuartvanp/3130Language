# ENGG3130-W20 Modelling Complex Systems
## Final Project: Twitter Summarizer

### Group:
- Scott Ackerl
- Stuart van Pinxteren
- Paige Phillips
- Sebastian McLearon


### What is your project about?

The purpose of this project is identify how to usefully summarize a set of text data using Natural Language Processing (NLP) models in Python.
For this case, we have decided to show the use case of such a summarizer by summarizing tweets. Another interesting use case for this type of summarizer would be for reducing the complexity of terms and conditions pages.
The purpose of the project is to remove opinion from tweets, and summarize many tweets about a certain topic down to one. 

### What is the baseline experiment?  

Feed the NLP model with a set of twitter data, and try to get it to summarize the data effectively.

An example of this will be to follow a trending/specific twitter hashtag (The Oscars, Coronavirus, etc.).

### How are you going to gauge the limitations of your model?  

- Try it on more technical tweets (more numbers, links, photos, videos, etc.)
- See how poorly the model does without being selective about which accounts to summarize from.

### To Do

1. Figure out how to scrape tweets, or use an existing twitter scraper
2. Figure out how to use a NLP model to create a summarizer, or use an existing summarizer implementation and tweak it to work.
3. Adjust the scraper and summarizer to produce useful results.

### Progress
#### tweet scraping: 
This website has alot of the functionality we would need to collect data. It seems to struggle collecting tweets based off of a query, but does seems to perform fine when scraping tweets from a specific twitter account

http://tools.mercenie.com/social/tweet-scraper/?fbclid=IwAR3f_XtmUEkQ9gop4aGcPvMcxIdRqG1aV4zF_28ZVlO-eev8trN6XHNLLNA
****

This repo, twitterscraper may also do the work we need done. It does not rely off of the twitter API so there is no limitations as to how many tweets can be scraped in a given time period. Stuart is currently testing its functionality. its output is generally in the form of a JSON file, which is very parsable but ideally we would not be using any Javascript in this project.

* example of scraper output can be seen in repo front page, this was done with a search for "tom brady AND buccaneers" with tweets over 100 likes

##### Things im trying to figure out right now
* how to limit the number of tweets scraped, the -l command given by the repo doesnt seem to work
* tweet validation, there is a ton of crap on twitter, currently trying to parse by number of likes and retweets to see if content is actually worth reading
* getting tweets that are only in enlgish, most likely done by choosing topics that have the highest relevance in north america



https://github.com/taspinar/twitterscraper


