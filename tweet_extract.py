
import tweepy

access_token_key = ""  
access_token_secret = ""

consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token_key,access_token_secret)
api = tweepy.API(auth)

user= "Edulixing" 


#all status updates from user.
#COST: 1 API call= 20 users
for status in tweepy.Cursor(api.user_timeline, id=user).items(5000):
    #status is an object with many fields and info
    print status.text
    
