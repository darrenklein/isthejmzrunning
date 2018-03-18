from google.transit import gtfs_realtime_pb2
import urllib.request
import env_variables

class NewRequest:
    # Initialize the new request by generating the unique request url
    def __init__(self, query_param):
        self.request_url = f'http://datamine.mta.info/mta_esi.php?key={env_variables.MTA_API_KEY}&feed_id={query_param}'

    # The actual get request - both gets the data and processes it into a list of entities.
    # Inspired by https://developers.google.com/transit/gtfs-realtime/examples/python-sample
    def get(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        response = urllib.request.urlopen(self.request_url)
        feed.ParseFromString(response.read())
        return [entity for entity in feed.entity]