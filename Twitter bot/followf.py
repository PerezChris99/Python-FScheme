import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Getting and following back followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Witing...")
        time.sleep(60)

if __name__ == "__main__":
    main()