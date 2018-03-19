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
# The list of train lines that we want to return.
# "'status': False" will imply no delay - .assess_alerts() will be used to change that...
line_list = [
    {
        'routeId': 'j',
        'status': False
    },
    {
        'routeId': 'm',
        'status': False
    },
    {
        'routeId': 'z',
        'status': False
    }
]

@app.route('/')
def index():
    bdfm_request = MTARequest.NewRequest(bdfm_feed_id).get()
    jz_request = MTARequest.NewRequest(jz_feed_id).get()
    alert_data = HandleData.check_results_for_alerts(bdfm_request, jz_request)
    line_statuses = HandleData.assess_alerts(alert_data, line_list)
    return render_template('index.html', lineStatuses=line_statuses)
