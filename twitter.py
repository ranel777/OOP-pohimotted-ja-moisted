class Tweet:
    def __init__(self, user: str, content: str, time: float, retweets: int):
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets

    def __repr__(self):
        return f"Tweet by @{self.user} at time {self.time}: {self.content} (Retweets: {self.retweets})"

    def get_hashtags(self):
        return [word for word in self.content.split() if word.startswith('#')]

def find_fastest_growing(tweets: list) -> Tweet:
    return max(tweets, key=lambda tweet: tweet.retweets / tweet.time)

def sort_by_popularity(tweets: list) -> list:
    sorted_tweets = sorted(tweets, key=lambda tweet: (-tweet.retweets, tweet.time))
    return sorted_tweets

def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    return [tweet for tweet in tweets if hashtag in tweet.get_hashtags()]

def sort_hashtags_by_popularity(tweets: list) -> list: 
    hashtag_popularity = {}
    
    for tweet in tweets:
        for hashtag in tweet.get_hashtags():
            if hashtag not in hashtag_popularity:
                hashtag_popularity[hashtag] = 0
            hashtag_popularity[hashtag] += tweet.retweets
    
    sorted_hashtags = sorted(hashtag_popularity.items(), key=lambda item: item[1], reverse=True)
    
    return [hashtag for hashtag, _ in sorted_hashtags]
