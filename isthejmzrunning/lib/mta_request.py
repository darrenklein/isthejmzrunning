from google.transit import gtfs_realtime_pb2
import urllib.request
import env_variables

class NewRequest:
    def __init__(self, query_param):
        self.request_url = f'http://datamine.mta.info/mta_esi.php?key={env_variables.MTA_API_KEY}&feed_id={query_param}'

    def get(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        response = urllib.request.urlopen(self.request_url)
        feed.ParseFromString(response.read())
        return feed