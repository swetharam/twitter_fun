import tweepy
from textblob import TextBlob
consumer_key= '################'
consumer_secret='################'

access_token='################'
access_token_secret='################'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)


#actual code for simple twitter bot that read a file and updates the contents of the file as a tweet
api=tweepy.API(auth)
#the newtweet is a file which has the contents
def retweets():
    f= open("newtweet","r")
    filedata=f.readlines()
    f.close()
    for lines in filedata:
        #you get an error when this condition is not included
        if lines!="\n":
            api.update_status(lines)
            print(lines)
        else:
            break

# retweets()
f=open("data","w")
#searching twitter for a particular hashtag
for tweet in tweepy.Cursor(api.search,q='#cartoons').items(1):
    # print(tweet.text)
    # print(tweet.user.screen_name)
    print("Tweet by "+tweet.user.name)
    # tweet.retweet()
    print("Retweeted this tweet")
    # print(tweet.user.followers_count,tweet.user.friends_count)
    tweet.favorite()
    tweet.user.follow()


