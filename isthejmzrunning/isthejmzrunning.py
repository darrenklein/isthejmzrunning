from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import isthejmzrunning.lib.mta_request as MTARequest
import isthejmzrunning.lib.handle_data as HandleData
import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ISTHEJMZRUNNING_SETTINGS', silent=True)

# feed_ids taken from http://datamine.mta.info/list-of-feeds
bdfm_feed_id = '21'
jz_feed_id = '36'

# The list of train lines that we want to return
route_list = ['J', 'M', 'Z']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch')
def fetch():
    bdfm_request = MTARequest.NewRequest(bdfm_feed_id).get()
    jz_request = MTARequest.NewRequest(jz_feed_id).get()
    route_info = HandleData.process_results(bdfm_request, jz_request)
    route_statuses = HandleData.assess_results(route_info, route_list)

    return json.dumps(route_statuses)