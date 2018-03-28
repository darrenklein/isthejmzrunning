import itertools
import json

# The aim of this function is to examine the feed data and output a tuple of two lists -
# The first list will contain a list of all of the train lines currently running (tripUpdate),
# the second list will contain all of the lines for which there is a delay alert.
def process_results(entity_lists):
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

    # Flatten the lists and put them into a dictionary for easy processing by assess_results()
    return {
        'current_trips': list(itertools.chain.from_iterable(current_trips)),
        'alerted_routes': list(itertools.chain.from_iterable(alerted_routes))
    }

# Loop through the line_list, checking to see if the line is either not present in the current trips
# or present in the alerted lines, implying that a train is either not running or delayed, respectively.
def assess_results(route_info, route_list):
    results = []

    for route in route_list:
        route_dic = {
            'route_id': route
        }
        if route not in route_info['current_trips']:
            route_dic['not_running'] = True
        elif route in route_info['alerted_routes']:
            route_dic['delay_status'] = True

        results.append(route_dic)

    return results
