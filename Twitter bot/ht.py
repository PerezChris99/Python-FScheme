#Hello tweepy bot
import tweepy
import json

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

#methods for users
user = api.get_user("MikezGarcia")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 50 Followers:")
for follower in user.followers():
    print(follower.name)

#methods for followers
api.create_friendship("realpython")

#methods for your account
api.update_profile(description="I Like Python")

#methods for likes
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"liking tweet {tweet.id} of {tweet.author.name}")
api.create_favourite(tweet.id)

#methods for blocking users
for block in api.blocks():
    print(block.name)

#methods for searches
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

#methods for trends
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

#methods for streaming

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

#authenticate to twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "COMSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

#create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Flask", "Django"], languages=["en"])

#fetching every tweet in which the account is mentioned
tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favourite()
    tweet.user.follow()




