import json
import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

from .game_data_store import choices


def home(request):
    return render(request, 'text_game/home.html')


def load_game(request):

    # TODO
    # Do any initial setup for the game here. If you want to save game state for 
    # a user, create a GameState object for that user. You can update it in the 
    # user_action 


    jsonData = choices.get_next_choice(0)
    return JsonResponse(jsonData)



def user_action(request):
  
    if request.method == 'POST':

        # TODO update user's game progress, as stored in the database 

        request_data = json.loads(request.body)
        next_text = request_data.get('next_text')

        print(request_data,next_text)

        
        
        if next_text 
        
        else:
            return JsonResponse( {"message": "Sorry, the game is not yet finished." } )




        
    else:
        return HttpResponseNotAllowed()   # No get requests, only POST, since these requests may affect the state of the data stored on the server. 