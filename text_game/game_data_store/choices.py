import os 
import json 


def get_next_choice(next_choice_id):
    # todo figure out what JSON file to open, return actual choices
    # for next_choice_id 

    # All file paths are relative to manage.py
    # use path.join to join folders in a operating-system neutral way
    path = os.path.join('text_game', 'game_data_store','json', 'choices.json')


    with open(path) as jsonFile:
        jsonData = json.load(jsonFile)

    # The view must return an object, not a list. So covert here, on on your view
    jsonOb = jsonData[next_choice_id]  # or do this in the view or adjust the structure of the JSON in the file
    return jsonOb 