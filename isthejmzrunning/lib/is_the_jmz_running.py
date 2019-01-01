from .mta_request import NewRequest

# Kicks off the process - for each feed_id, instantiate a NewRequest object and make
# a GET request to that URL.
def initialize_fetch(feed_ids):
    entity_lists = []

    for feed_id in feed_ids:
        try:
            entity_lists.append(NewRequest(feed_id).get())
        except:
            return False

    return entity_lists
