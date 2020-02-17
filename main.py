from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
from time import mktime
from dateutil.tz import tzlocal
from feed_urls import *
import feedparser, pytz, os, urllib.parse, gc, timeit, pylibmc, redis
from ast import literal_eval
#force SSL
from flask_sslify import SSLify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'N0NE'
try:
    redis_db = redis.from_url(os.environ.get("REDIS_URL"))
except:
    print("No redis database URL set")

if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)

###Views Code Begins

##Render the basic layout 

all_links = dict(new = news_links, tec = tech_links, biz = biz_links, \
    rel = religious_links, spo = sport_links, lei = leisure_links, \
    muz = music_links)

@app.route('/')
def index():
    return render_template('main.html')

##Render the content
###This function is called by the AJAX.js script to render content based on category
@app.route('/color')
def color():
    category = request.args.get('target', 'news', type=str)
    cur_category = redis_db.get(category)
    return render_template('content.html', parsed=cur_category)

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

##Functions to parse and store links

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
        redis_db.set(link_category, output_data)
        print(link_category + " saved")
'''
def singler(link_set):
    current_set = all_links[link_set]
    output_data = list()
    for object in current_set:
        output_data.append(parser(object))
        print((object.source))
    ##Send key-value dict() to database via POST
    redis_db.set(link_set, output_data)
    print(link_set + "saved")
'''

###Start the app here

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=False)

