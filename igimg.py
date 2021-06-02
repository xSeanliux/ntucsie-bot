import instaloader, random, os

def query(hashtag):
    session = instaloader.Instaloader()
    session.login(user = "ais3.202001", passwd = os.getenv("IG_PASSWORD"))

    jsonData = session.context.get_json(path="explore/tags/" + hashtag + "/", params={"__a": 1})
    
    hasNextPage = True
    pageNumber = 1
    urls = []
    while hasNextPage:
        if pageNumber > 1 : break
        print("Page " + str(pageNumber))
        sections = jsonData['data']['recent']['sections']

        for section in sections:
            for post in section['layout_content']['medias']:
                try:    
                    urls.append((post["media"]["image_versions2"]["candidates"][0]["url"], post["media"]["code"]))
                except:
                    pass

        hasNextPage = jsonData['data']['recent']['more_available']
        if hasNextPage:
            jsonData = session.context.get_json(
                path="explore/tags/" + hashtag + "/",
                params={"__a": 1,
                        "max_id": jsonData['data']['recent']['next_max_id']}
            )
        pageNumber += 1
    urls = list(set(urls))
    url = random.choice(urls)
    print(url, len(urls))
    return url

if __name__ == '__main__':
    query("拉麵")
    