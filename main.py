from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
from time import mktime
#from tzlocal import get_localzone
from feed_urls import *
import feedparser, pytz, os, urllib.parse
from ast import literal_eval
import gc
import timeit
import pylibmc
from flask_caching import Cache
from flask_sslify import SSLify


mc = Cache()
app = Flask(__name__)

if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)

#connect to memecache servers
cache_servers = os.environ.get('MEMCACHIER_SERVERS')
cache_user = os.environ.get('MEMCACHIER_USERNAME') or ''
cache_pass = os.environ.get('MEMCACHIER_PASSWORD') or ''
mc.init_app(app,
    config={'CACHE_TYPE': 'saslmemcached',
            'CACHE_MEMCACHED_SERVERS': cache_servers.split(','),
            'CACHE_MEMCACHED_USERNAME': cache_user,
            'CACHE_MEMCACHED_PASSWORD': cache_pass,
            'CACHE_OPTIONS': { 'behaviors': {
                # Faster IO
                'tcp_nodelay': True,
                # Keep connection alive
                'tcp_keepalive': True,
                # Timeout for set/get requests
                'connect_timeout': 2000, # ms
                'send_timeout': 750 * 1000, # us
                'receive_timeout': 750 * 1000, # us
                '_poll_timeout': 2000, # ms
                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30}}})
###Views Code Begins

##Render the basic layout 

all_links = dict(new = news_links, tec = tech_links, biz = biz_links, \
    rel = religious_links, spo = sport_links, lei = leisure_links, \
    muz = music_links)

@app.route('/')
def index():
    return render_template('main.html')

##Render the content

@app.route('/build')
def build():
    if mc.get('muz') == None:
        #print("Build completed in %f seconds." % \
        #    timeit.timeit(reloader, number=1))
        timer_str = "Build completed in %f seconds." % timeit.timeit(reloader, number=1)
        return timer_str
    else:
        return 'cached'

@app.route('/forcebuild')
def forcebuild():
    return "Build completed in %f seconds." % timeit.timeit(reloader, number=1)


###This function is called by the AJAX.js script to render content based on category
@app.route('/color')
def color():
    category = request.args.get('target', 'news', type=str)
    cur_category = mc.get(category)
    return render_template('content.html', parsed=cur_category)

##Parse the RSS feeds 
def parser(link):
    d = feedparser.parse(link.location)
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
        try:
            f_title = d.entries[item_count].title.split()[:8]
            tmp = dict(full_title = d.entries[item_count].title, title = ' '.join(f_title), link = d.entries[item_count].link, pub = f_dt)
        except:
            print(link.source)
        parsed_items.append(tmp)
    return dict(source = link.source, data = parsed_items)

##Use to build the cache 

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
        ##Set the memcache
        mc.set(link_category, output_data)
        print(link_category + " saved")

def singler(link_set):
    current_set = all_links[link_set]
    output_data = list()
    for object in current_set:
        output_data.append(parser(object))
        print((object.source))
        ##Set the memcache
    mc.set(link_set, output_data)
    print(link_set + "saved")

###Start the app here

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=False)

