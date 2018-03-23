import itertools
import json

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
            # Worth noting that in some instances, an alert occurs with no informedEntity.
            if 'informedEntity' in entity.get('alert'):
                informed_entities = entity.get('alert').get('informedEntity')
                alert_data = [informed_ent.get('trip').get('routeId') for informed_ent in informed_entities]
                alerted_routes.append(alert_data)

    # Flatten the lists and put them into a tuple for easy processing by assess_results()
    return (list(itertools.chain.from_iterable(current_trips)), list(itertools.chain.from_iterable(alerted_routes)))

# Loop through the line_list, checking to see if the line is either not present in the current trips
# (line_info[0]) or present in the alerted lines (line_info[1]), implying that a train is either not
# running or delayed, respectively.
def assess_results(line_info, line_list):
    results = []

    for line in line_list:
        line_dic = {
            'route_id': line
        }
        if line not in line_info[0]:
            line_dic['not_running'] = True
        elif line in line_info[1]:
            line_dic['delay_status'] = True

        results.append(line_dic)

    return results
