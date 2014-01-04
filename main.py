from flask import Flask, request, redirect, url_for, render_template
from werkzeug.contrib.cache import SimpleCache 
from datetime import datetime
from time import mktime
from tzlocal import get_localzone
from feed_urls import *
import feedparser, pytz

app = Flask(__name__)

###initialize Cache

cache = SimpleCache()

###Views Code Begins

##Render the basic layout 

all_links = dict(new = news_links, tec = tech_links, biz = biz_links, \
    rel = religious_links, spo = sport_links, lei = leisure_links, muz = music_links)


@app.route('/')
def index():
    return render_template('main.html')

##Receive the AJAX request and render the content

@app.route('/color')
def color():
    color = request.args.get('target', 'news', type=str)
    testing = cache.get(color)
    if testing is None:
        testing = parse(all_links[color])
        cache.set(color, testing, timeout=10*60)
    return render_template('content.html', parsed=testing)

##Parse the RSS feeds 

def parse(links):
    all_items = list()
    for link in links:
        d = feedparser.parse(link['locate'])
        parsed_items = list()
        for item_count in range(0,10):
            try:
                dt = datetime.fromtimestamp(mktime(d.entries[item_count].published_parsed))
                dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(get_localzone())
                f_dt = datetime.strftime(dt_1, "%B %d | %I:%M %p")
            except:
                f_dt = 'A Time Unknown'
            f_title = d.entries[item_count].title.split()[:8]
            tmp = dict(full_title = d.entries[item_count].title, title = ' '.join(f_title), link = d.entries[item_count].link, pub = f_dt)
            parsed_items.append(tmp)
        all_items.append(dict(source = link['source'], data = parsed_items))
    return all_items

##Use to build the cache using the Scheduler add-on

def reload(group):
    for link_set in group:
        rss_data = parse(link_set)
        cache.set('name', rss_data, timeout=10*60)

###Start the app here

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=port, debug=False)