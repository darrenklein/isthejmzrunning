from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import isthejmzrunning.lib.mta_request as MTARequest

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ISTHEJMZRUNNING_SETTINGS', silent=True)

# feed_ids taken from http://datamine.mta.info/list-of-feeds
bdfm_feed_id = '21'
jz_feed_id = '36'

@app.route('/')
def index():
    bdfm_request = MTARequest.NewRequest(bdfm_feed_id).get()
    jz_request = MTARequest.NewRequest(jz_feed_id).get()
    print(bdfm_request)
    print(jz_request)
    return render_template('index.html')






# @app.route('/')
# def index():
#     # taken from https://developers.google.com/transit/gtfs-realtime/examples/python-sample
#     feed = gtfs_realtime_pb2.FeedMessage()
#     response = urllib.request.urlopen(f'http://datamine.mta.info/mta_esi.php?key={env_variables.MTA_API_KEY}&feed_id={jz_feed_id}')
#     feed.ParseFromString(response.read())

#     for entity in feed.entity:
#         print(entity)
#         # if hasattr(entity.alert.informed_entity, 'trip'):
#         #     route_id = entity.alert.informed_entity.trip.route_id
#         #     print(f'There\'s a delay on the {route_id} train!')
#         # else:
#         #     print('all good')

#     return render_template('index.html')