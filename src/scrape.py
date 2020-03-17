# ------------------------------------

# Uses twitter scraper python library dependency
# Install with:

# pip install twitterscraper

# ------------------------------------

from twitterscraper import query_tweets

if __name__ == '__main__':

	#print the retrieved tweets to the screen:
	file = open("output.txt", "w")
	for tweet in query_tweets("Trump", 1):
		file.write(tweet.text + "\n\n")
	file.close()

