from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from google.transit import gtfs_realtime_pb2
import urllib.request
import env_variables

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ISTHEJMZRUNNING_SETTINGS', silent=True)

bdfm_feed_id = '21'
jz_feed_id = '36'

@app.route('/')
def index():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urllib.request.urlopen(f'http://datamine.mta.info/mta_esi.php?key={env_variables.MTA_API_KEY}&feed_id={jz_feed_id}')
    feed.ParseFromString(response.read())

    print(feed)

    # for entity in feed.entity:
    #     print(entity)

    return render_template('index.html')