import itertools
import json

# We'll receive two entity_lists - one for the BDFM lines, and one for the JZ lines.
# To make this code more reusable, use the * prefixed argument and then use the itertools
# to join all of the results into one long list to check.
# This function will output a list of alerted lines, of which there may be duplicate values.
def check_results_for_alerts(*entity_lists):
    # Concat all of the result lists into one list
    entity_list = list(itertools.chain.from_iterable(entity_lists))
    for entity in entity_list:
        # Convert the JSON string to a dict
        entity = json.loads(entity)
        # If there's an alert entity, this will (likely) contain our delay notifications
        if 'alert' in entity:
            print('alert found')
            print(entity)
            # It seems that delay notifications don't always correspond to a line.
            # If the entity has informedEntity info, that'll have the line info.
            if 'informedEntity' in entity.get('alert'):
                informed_entities = entity.get('alert').get('informedEntity')
                alerted_routes = [informed_ent.get('trip').get('routeId') for informed_ent in informed_entities]
                print(f'alerted routes: {alerted_routes}')
                return alerted_routes
            # Not sure how to interpret lineless delay info... for now, have to leave it at this.
            else:
                print('alert found, no lines specified')
                return []
        else:
            print('no alerts found')
            return []

# Loop through the alert data and compare it with the line_list
def assess_alerts(alert_data, line_list):
    for line in line_list:
        if line.get('routeId') in alert_data:
            line['status'] = True
    return line_list
