from twitterscraper import query_tweets
import datetime as dt

f= open("tweets.txt","w+")
i = 0;

for tweet in query_tweets("Tom Brady AND Buccaneers", limit = 1000, begindate=dt.date(2020, 3, 15)):

    if (tweet.likes > 100):
    	f.write(tweet.text)


    	if (tweet.is_reply_to):
    		pass
    	if (i > 10):
    		break
    	i += 1
    	f.write("\n")
    	f.write("\n")
f.close()