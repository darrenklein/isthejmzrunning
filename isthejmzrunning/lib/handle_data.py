import itertools
import json

# We'll receive two entity_lists - one for the BDFM lines, and one for the JZ lines.
# To make this code more reusable, use the * prefixed argument and then use the itertools
# to join all of the results into one long list to check.
# This function will output a list of alerted lines, of which there may be duplicate values.
def check_results_for_alerts(*entity_lists):
    # Concat all of the result lists into one list
    entity_list = list(itertools.chain.from_iterable(entity_lists))
    alerted_routes = []
    for entity in entity_list:
        # Convert the JSON string to a dict
        entity = json.loads(entity)
        # If there's an alert entity, this will (likely) contain our delay notifications
        if 'alert' in entity:
            print('alert found')
            print(entity)
            # It seems that delay notifications don't always correspond to a line.
            # If the entity has informedEntity info, that'll have the line info.
            # Pull the route numbers out of the informedEntity and append the list to alerts.
            if 'informedEntity' in entity.get('alert'):
                informed_entities = entity.get('alert').get('informedEntity')
                alert_data = [informed_ent.get('trip').get('routeId') for informed_ent in informed_entities]
                alerted_routes.append(alert_data)
            # Not sure how to interpret lineless delay info... for now, have to leave it at this.
            else:
                print('alert found, no routeId specified')

    # Flatten the list of lists for easy processing by assess_alerts
    return list(itertools.chain.from_iterable(alerted_routes))

def check_results_for_current_trips(*entity_lists):
    entity_list = list(itertools.chain.from_iterable(entity_lists))
    current_trips = []
    for entity in entity_list:
        entity = json.loads(entity)
        if 'tripUpdate' in entity:
            current_trips.append(entity.get('tripUpdate').get('trip').get('routeId'))

    return list(itertools.chain.from_iterable(current_trips))


# Loop through the alert data and compare it with the line_list
def assess_alerts(alerted_routes, line_list):
    for line in line_list:
        if line.get('route_id') in alerted_routes:
            line['delay_status'] = True
    return line_list

def assess_current_trips(current_trips, line_list):
    for line in line_list:
        if line.get('route_id') not in current_trips:
            line['not_running'] = True
    return line_list

