from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import isthejmzrunning.lib.mta_request as MTARequest
import isthejmzrunning.lib.handle_data as HandleData

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ISTHEJMZRUNNING_SETTINGS', silent=True)

# feed_ids taken from http://datamine.mta.info/list-of-feeds
one_feed_id = '1'
a_feed_id = '26'
n_feed_id = '16'
l_feed_id = '2'
g_feed_id = '31'
seven_feed_id = '51'
bdfm_feed_id = '21'
jz_feed_id = '36'
# The list of train lines that we want to return.
# "'delay_status': False" will imply no delay - .assess_alerts() will be used to change that...
route_list = [
    # {
    #     'route_id': '1',
    #     'delay_status': False
    # },
    # {
    #     'route_id': '2',
    #     'delay_status': False
    # },
    # {
    #     'route_id': '3',
    #     'delay_status': False
    # },
    # {
    #     'route_id': '4',
    #     'delay_status': False
    # },
    # {
    #     'route_id': '5',
    #     'delay_status': False
    # },
    # {
    #     'route_id': '6',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'GS',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'A',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'C',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'E',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'N',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'Q',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'R',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'L',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'G',
    #     'delay_status': False
    # },
    # {
    #     'route_id': 'W',
    #     'delay_status': False
    # },
    # {
    #     'route_id': '7',
    #     'delay_status': False
    # },
    {
        'route_id': 'B',
        'delay_status': False,
        'not_running': False
    },
    {
        'route_id': 'D',
        'delay_status': False,
        'not_running': False
    },
    {
        'route_id': 'F',
        'delay_status': False,
        'not_running': False
    },
    # {
    #     'route_id': 'J',
    #     'delay_status': False
    # },
    {
        'route_id': 'M',
        'delay_status': False,
        'not_running': False
    },
    # {
    #     'route_id': 'Z',
    #     'delay_status': False
    # }
]

@app.route('/')
def index():
    # one_request = MTARequest.NewRequest(one_feed_id).get()
    # a_request = MTARequest.NewRequest(a_feed_id).get()
    # n_request = MTARequest.NewRequest(n_feed_id).get()
    # l_request = MTARequest.NewRequest(l_feed_id).get()
    # g_request = MTARequest.NewRequest(g_feed_id).get()
    # seven_request = MTARequest.NewRequest(seven_feed_id).get()

    bdfm_request = MTARequest.NewRequest(bdfm_feed_id).get()
    # jz_request = MTARequest.NewRequest(jz_feed_id).get()

    # alerted_routes = HandleData.check_results_for_alerts(bdfm_request, jz_request, one_request, a_request, n_request, l_request, g_request, seven_request)

    alerted_routes = HandleData.check_results_for_alerts(bdfm_request)

    current_trips = HandleData.check_results_for_current_trips(bdfm_request)

    # alerted_routes = HandleData.check_results_for_alerts(bdfm_request, jz_request)

    line_statuses = HandleData.assess_alerts(alerted_routes, route_list)
    current_trip_statuses = HandleData.assess_current_trips(current_trips, route_list)

    print('jook')
    print(current_trip_statuses)


    return render_template('index.html', lineStatuses=line_statuses)
