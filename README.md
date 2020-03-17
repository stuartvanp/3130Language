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
