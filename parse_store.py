import redis, json


try:
    redis_db = redis.from_url(os.environ.get("REDIS_URL"))
except:
    print("No redis database URL set")

##Functions to parse and store links

all_links = dict(new = news_links, tec = tech_links, biz = biz_links, \
    rel = religious_links, spo = sport_links, lei = leisure_links, \
    muz = music_links)

def reloader():
    for link_category in all_links:
        current_set = all_links[link_category]
        output_data = list()
        for object in current_set:
          try:
            output_data.append(parser(object))
            print((object.source))
          except:
            print(object.source + " failed")
        ##Send key-value dict() to redis database
        format_data = json.dumps(output_data)
        redis_db.set(link_category, format_data)
        print(link_category + " saved")
