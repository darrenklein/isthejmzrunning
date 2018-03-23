from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import isthejmzrunning.lib.mta_request as MTARequest
import isthejmzrunning.lib.handle_data as HandleData

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ISTHEJMZRUNNING_SETTINGS', silent=True)

# feed_ids taken from http://datamine.mta.info/list-of-feeds
bdfm_feed_id = '21'
jz_feed_id = '36'

# The list of train lines that we want to return
line_list = ['J', 'M', 'Z']

@app.route('/')
def index():
    bdfm_request = MTARequest.NewRequest(bdfm_feed_id).get()
    jz_request = MTARequest.NewRequest(jz_feed_id).get()

    line_info = HandleData.process_results(bdfm_request, jz_request)
    line_statuses = HandleData.assess_results(line_info, line_list)

    return render_template('index.html', lineStatuses=line_statuses)
