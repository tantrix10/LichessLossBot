import requests as r
import lichess.api as api
import twitter
from time import sleep

from secrets import consumer_key, consumer_secret_key, access_token, access_token_secret
# ;'s are just beacuse I keep forgetting them in ; langs and python doens't care


connection = twitter.Twitter(
    auth = twitter.OAuth(
        access_token,
        access_token_secret,
        consumer_key,
        consumer_secret_key,
    ));
POSTED_GAMES = set();

# Yeah magic number-y, will break out into config
last_time_stamp = 1611923887810;
user = "dobbo";

def check_win(game):
    """
    Take a game dict and return true if user lost.
    """
    if game['players']['white']['user']['id'] == user:
        colour = "white"
    else:
        colour = "black"
    return game['winner'] != colour

def generate_tweet(game):
    """
    Generate and return tweet string from game dict.
    """
    string = f"{user} lost a {game['speed']} game. Check it out: https://lichess.org/{game['id']}"
    return string

while True:
    games = list(api.user_games(user, since=last_time_stamp));
    lost_games = [game for game in games if check_win(game)];
    loses_to_be_posted = [game for game in lost_games if game["id"] not in POSTED_GAMES]
    if loses_to_be_posted:
        print(loses_to_be_posted);
        print([game["lastMoveAt"] for game in loses_to_be_posted]);
        last_time_stamp = max(game["lastMoveAt"] for game in loses_to_be_posted);
        [POSTED_GAMES.add(game["id"]) for game in loses_to_be_posted];

        tweets = [generate_tweet(game) for game in loses_to_be_posted];
        print(tweets)
        [connection.statuses.update(status=tweet) for tweet in tweets]
        # query once an hour
    sleep(60*60);
