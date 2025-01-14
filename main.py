from app.twitter_bot import create_twitter_client, process_mentions
from time import sleep

if __name__ == "__main__":
    client = create_twitter_client()
    while True:
        try:
            process_mentions(client)
        except Exception as e:
            print(f"Error: {e}")
        sleep(60)  # Check for mentions every minute
