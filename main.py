from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
from time import mktime, clock
#from tzlocal import get_localzone
from feed_urls import *
import feedparser, pytz, os, urlparse, bmemcached, json
from ast import literal_eval
from multiprocessing.pool import ThreadPool
import gc
import timeit

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
        print "Build completed in %f seconds." % \
            timeit.timeit(reloader, number=1)
    else:
        return 'cached'

@app.route('/forcebuild')
def forcebuild():
    return "Build completed in %f seconds." % timeit.timeit(reloader, number=1)

@app.route('/color')
def color():
    color = request.args.get('target', 'news', type=str)
    testing = mc.get(color)
    return render_template('content.html', parsed=testing)

##Parse the RSS feeds 

def parse(links):
    pool = ThreadPool(5)
    return pool.map(parse_helper, links)

# Spawn a thread for each link
# TODO In the future, it could be worth combining this somehow with the linkset
#      to prevent extraneous thread spawns.
def parse_helper(link):
    d = feedparser.parse(link['locate'])
    parsed_items = list()
    for item_count in range(0,10):
        try:
            dt = datetime.fromtimestamp(mktime(d.entries[item_count].published_parsed))
            #dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/New_York'))
            dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/Los_Angeles'))
            #dt_1 = dt.replace(tzinfo=pytz.utc).astimezone(get_localzone())
            f_dt = datetime.strftime(dt_1, "%B %d | %I:%M %p")
        except:
            f_dt = 'A Time Unknown'
        f_title = d.entries[item_count].title.split()[:8]
        tmp = dict(full_title = d.entries[item_count].title, title = ' '.join(f_title), link = d.entries[item_count].link, pub = f_dt)
        parsed_items.append(tmp)
    return dict(source = link['source'], data = parsed_items)

##Use to build the cache 

# Spawn a thread for each link set
def reloader():
    pool = ThreadPool(5)
    pool.map(reloader_helper, all_links)

def reloader_helper(link_set):
    cur_set = all_links[link_set]
    rel_tmp = parse(cur_set)
    ##Set the memcache
    mc.set(link_set, rel_tmp)

###Start the app here

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=False)

