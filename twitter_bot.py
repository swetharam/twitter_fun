import tweepy
#the following lines are for authenticating
consumer_key= '**********************'
consumer_secret='***********************'

access_token='************************'
access_token_secret='****************************'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#actual code for simple twitter bot that read a file and updates the contents of the file as a tweet
api=tweepy.API(auth)
#the newtweet is a file which has the contents
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

