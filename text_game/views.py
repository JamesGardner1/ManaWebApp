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

        
        
        if next_text == '1':
            jsonData = choices.get_next_choice(1)
            return JsonResponse(jsonData)

        
        elif next_text == '2':
            jsonData = choices.get_next_choice(2)
            return JsonResponse(jsonData)

        
        elif next_text == '3':
            jsonData = choices.get_next_choice(3)
            return JsonResponse(jsonData)
        
        elif next_text == '4':
            jsonData = choices.get_next_choice(4)
            return JsonResponse(jsonData)

        elif next_text == '5':
            jsonData = choices.get_next_choice(5)
            return JsonResponse(jsonData)

        elif next_text == '6':
            jsonData = choices.get_next_choice(6)
            return JsonResponse(jsonData)

        elif next_text == '7':
            jsonData = choices.get_next_choice(7)
            return JsonResponse(jsonData)
        
        elif next_text == '8':
            jsonData = choices.get_next_choice(8)
            return JsonResponse(jsonData)

        elif next_text == '9':
            jsonData = choices.get_next_choice(9)
            return JsonResponse(jsonData)

        elif next_text == '10':
            jsonData = choices.get_next_choice(10)
            return JsonResponse(jsonData)
        
                
    
        else:
            return JsonResponse( {"message": "Sorry, the game is not yet finished." } )




        
    else:
        return HttpResponseNotAllowed()   # No get requests, only POST, since these requests may affect the state of the data stored on the server. 