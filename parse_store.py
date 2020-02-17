from datetime import datetime
from time import mktime
from dateutil.tz import tzlocal
from feed_urls import *
import feedparser, redis, json, os


try:
    redis_db = redis.from_url(os.environ.get("REDIS_URL"))
except:
    print("No redis database URL set")

##Functions to parse and store links

all_links = dict(new = news_links, tec = tech_links, biz = biz_links, \
    rel = religious_links, spo = sport_links, lei = leisure_links, \
    muz = music_links)

##Parse the RSS feeds 
def parser(link):
    d = feedparser.parse(link.location)
    parsed_items = list()
    for item_count in range(0,10):
        try:
            dt = datetime.fromtimestamp(mktime(d.entries[item_count].published_parsed))
            #dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/New_York'))
            #dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/Los_Angeles'))
            dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(tzlocal.get_localzone())
            f_dt = datetime.strftime(dt_1, "%B %d | %I:%M %p")
        except:
            f_dt = 'A Time Unknown'
        try:
            f_title = d.entries[item_count].title.split()[:8]
            tmp = dict(full_title = d.entries[item_count].title, title = ' '.join(f_title), link = d.entries[item_count].link, pub = f_dt)
        except:
            print(link.source)
        parsed_items.append(tmp)
    return dict(source = link.source, data = parsed_items)

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

reloader()
