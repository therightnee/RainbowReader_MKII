from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
from time import mktime, clock
from tzlocal import get_localzone
from feed_urls import *
import feedparser, pytz, os, urlparse, bmemcached, json
from ast import literal_eval

app = Flask(__name__)

###Initialize connection to cache

try:
    mc = bmemcached.Client(os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','), os.environ.get('MEMCACHEDCLOUD_USERNAME'), os.environ.get('MEMCACHEDCLOUD_PASSWORD'))

except:
    mc = bmemcached.Client('pub-memcache-19543.us-east-1-4.2.ec2.garantiadata.com:19543', 'memcached-app20933817', 'VNdVk1NpDX2WYTz5')



###Views Code Begins

##Render the basic layout 

all_links = dict(new = news_links, tec = tech_links, biz = biz_links, \
    rel = religious_links, spo = sport_links, lei = leisure_links, muz = music_links)

@app.route('/')
def index():
    return render_template('main.html')

##Render the content

@app.route('/build')
def build():
    if mc.get('muz') == None:
        reloader()
        return 'build'
    else:
        return 'cached'

@app.route('/color')
def color():
    color = request.args.get('target', 'news', type=str)
    testing = mc.get(color)
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

##Use to build the cache 
def reloader():
    for link_set in all_links:
        cur_set = all_links[link_set]
        rel_tmp = parse(cur_set)
        mc.set(link_set, rel_tmp)

###Start the app here

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=False)

