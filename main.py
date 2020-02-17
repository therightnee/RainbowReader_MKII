from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
from time import mktime
from dateutil.tz import tzlocal
from feed_urls import *
import feedparser, pytz, os, urllib.parse, gc, timeit, pylibmc, redis, json
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


@app.route('/')
def index():
    return render_template('main.html')

##Render the content
###This function is called by the AJAX.js script to render content based on category
@app.route('/color')
def color():
    category = request.args.get('target', 'news', type=str)
    #cur_category = redis_db.get(category)
    cur_category = json.loads(redis_db.get(category))
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

###Start the app here

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=False)

