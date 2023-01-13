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



