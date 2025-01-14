import tweepy

from config.config import (
    TWITTER_API_KEY, TWITTER_API_SECRET, 
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)

def create_twitter_client():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    return tweepy.API(auth)

def process_mentions(client):
    mentions = client.mentions_timeline(count=10)
    for mention in mentions:
        if "track" in mention.text.lower():
            wallet_address = extract_wallet_address(mention.text)
            if wallet_address:
                client.update_status(
                    f"@{mention.user.screen_name} Fetching data for {wallet_address}...",
                    in_reply_to_status_id=mention.id
                )
            else:
                client.update_status(
                    f"@{mention.user.screen_name} Invalid wallet address!",
                    in_reply_to_status_id=mention.id
                )

def extract_wallet_address(text):
    # Add logic to extract wallet address (e.g., regex for Ethereum addresses)
    return None
