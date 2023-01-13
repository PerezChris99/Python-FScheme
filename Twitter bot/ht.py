#Hello tweepy bot
import tweepy

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

api.update_status("Hello Tweepy")

#methods for users timeline
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

#method for tweets
api.update_status("Test tweet from tweepy python")



