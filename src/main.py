from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os

load_dotenv()

# Consumer api key
comsumer_api_key = os.getenv('CONSUMER_API_KEY')
# Consumer api secret key
comsumer_api_secret_key = os.getenv('CONSUMER_API_SECRET_KEY')
# bearer token
bearer_token = os.getenv('BEARER_TOKEN')
# Access token
access_token = os.getenv('ACCESS_TOKEN')
# Access token secret
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

url = "https://api.twitter.com/1.1/statuses/update.json"

params = {
    "status": "API Test",
    # "media[]": open("image.png", "rb")
}

TweetList = []

twitter = OAuth1Session(
    comsumer_api_key,
    comsumer_api_secret_key,
    access_token,
    access_token_secret)

req = twitter.post(url, params=params)
