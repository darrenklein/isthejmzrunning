from flask import Flask, render_template
from os import environ
import json
import isthejmzrunning.lib.handle_data as HandleData
import isthejmzrunning.lib.is_the_jmz_running as IsTheJMZRunning

app = Flask(__name__)

if environ.get('PRODUCTION') == 'True':
    app.config['MTA_API_KEY'] = environ.get('MTA_API_KEY')
else:
    app.config.from_envvar('DEV_CONFIG')

# feed_ids taken from http://datamine.mta.info/list-of-feeds
# These are for the BDFM and JMZ, respectively
feed_ids = ['21', '36']
# The list of train lines that we want to return to the UI
route_list = ['J', 'M', 'Z']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fetch')
def fetch():
    entity_lists = IsTheJMZRunning.initialize_fetch(feed_ids)

    if entity_lists:
        route_info = HandleData.process_results(entity_lists)
        route_statuses = HandleData.assess_results(route_info, route_list)
        return json.dumps(route_statuses)
    else:
        return json.dumps(False)

@app.errorhandler(404)
def not_found(_e):
    return render_template('not_found.html')
