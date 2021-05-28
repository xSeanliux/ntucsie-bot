import twitter, os, random

def query(query_str):
    api = twitter.Api(
        consumer_key = os.getenv("TWITTER_API_KEY"),
        consumer_secret = os.getenv("TWITTER_API_SECRET_KEY"),
        access_token_key = os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    results = api.GetSearch(
        raw_query="q={}&result_type=recent&count=50".format(query_str)
    )
    
    urls = []
    
    for res in results:
        try:
            url = res.media[0].media_url
            if url != None:
                urls.append(url)
        except:
            continue

    id = random.randint(0, len(urls) - 1)
    return urls[id]

if __name__ == "__main__":
    query("%23ぬいぐるみ撮影60分一本勝負")