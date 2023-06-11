from flask import Flask, request, render_template
import redis, json, os, urllib.parse
#force SSL
from flask_sslify import SSLify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'N0NE'

try:
    url = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL'))
    redis_db = redis.Redis(host=url.hostname, port=url.port, password=url.password)
except:
    print("No redis database URL set")

if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app)

###Views Code Begins

##Render the basic layout
@app.route('/')
def index():
    return render_template('main.html')

##Stuff the content
###This function is called by the AJAX.js script to render content based on category
@app.route('/color')
def color():
    category = request.args.get('target', 'news', type=str)
    cur_category = json.loads(redis_db.get(category))
    return render_template('content.html', parsed=cur_category)

###Start the app here

if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port, debug=False)
