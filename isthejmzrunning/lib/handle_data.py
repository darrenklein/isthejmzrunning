import itertools
import json
import copy

# The aim of this function is to examine the feed data and output a tuple of two lists -
# The first list will contain a list of all of the train lines currently running (tripUpdate),
# the second list will contain all of the lines for which there is a delay alert.
#
# We'll receive an entity_list for every feed_id request.
# To make this code more reusable, use the * prefixed argument and then use the itertools
# to join all of the results into one long list to check so any number of requests can be checked.
def process_results(*entity_lists):
    # Concat all of the result lists into one list
    entity_list = list(itertools.chain.from_iterable(entity_lists))
    current_trips = []
    alerted_routes = []

    for entity in entity_list:
        # Convert the JSON string to a dict
        entity = json.loads(entity)

        # If the entity is a tripUpdate, this train is currently running (somewhere)
        # Add the routeId to the list of current_trips
        if 'tripUpdate' in entity:
            current_trips.append(entity.get('tripUpdate').get('trip').get('routeId'))

        # If there's an alert entity, this will (likely) contain our delay notifications
        if 'alert' in entity:
            # It seems that delay notifications don't always correspond to a single line,
            # but will just occur once for every group of lines returned in the request and have
            # a list of the delayed lines.
            # If the entity has informedEntity info, that'll have the line info.
            # Pull the route numbers out of the informedEntity and append the list to alerts.
            if 'informedEntity' in entity.get('alert'):
                informed_entities = entity.get('alert').get('informedEntity')
                alert_data = [informed_ent.get('trip').get('routeId') for informed_ent in informed_entities]
                alerted_routes.append(alert_data)
            # Not sure how to interpret lineless delay info... for now, have to leave it at this.
            else:
                print('alert found, no routeId specified')

    # Flatten the lists and put them into a tuple for easy processing by assess_results()
    return (list(itertools.chain.from_iterable(current_trips)), list(itertools.chain.from_iterable(alerted_routes)))

# Loop through the line_list, checking to see if the line is either not present in the current trips
# (line_info[0]) or present in the alerted lines (line_info[1]), implying that a train is either not
# running or delayed, respectively.
def assess_results(line_info, line_list):
    # Create a deep copy so as to not mutate the original list
    line_list_copy = copy.deepcopy(line_list)

    for line in line_list_copy:
        if line.get('route_id') not in line_info[0]:
            line['not_running'] = True
        elif line.get('route_id') in line_info[1]:
            line['delay_status'] = True
    return line_list_copy
