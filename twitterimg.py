import twitter, os, random

def query(query_str):
    api = twitter.Api(
        consumer_key = os.getenv("TWITTER_API_KEY"),
        consumer_secret = os.getenv("TWITTER_API_SECRET_KEY"),
        access_token_key = os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    results = api.GetSearch(
        raw_query="q={}&result_type=recent&count=100".format(query_str)
    )
    urls = []
    
    for res in results:
        try:
            # get a tuple of (image url, tweet url])
            url = (res.media[0].media_url, res.media[0].expanded_url)
            if url != None:
                urls.append(url)
        except:
            continue
    urls = list(set(urls))
    url = random.choice(urls)
    print(url, len(urls))
    return url

if __name__ == "__main__":
    query("%23ぬいぐるみ撮影60分一本勝負")