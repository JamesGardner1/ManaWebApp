import json
import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

from .game_data_store import choices


travelerUnderRock = True
helpedFisherman = False


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

    travlerUnderRock = True
  
    if request.method == 'POST':

        # TODO update user's game progress, as stored in the database 

        request_data = json.loads(request.body)
        next_text = request_data.get('next_text')

        print(request_data,next_text)

        next_text_number = int(next_text)
        
        if next_text == 16:
            travelerUnderRock = False   
            # This should be stored in a cookie, or make the user sign in, and save this in a database for that user
            # Otherwise everyone playing the web app will have travelerUnderRock = False when this is set 
        

        if next_text_number >= 0:
            jsonData = choices.get_next_choice(next_text)
            return JsonResponse(jsonData)
        

        # This JSON could also be moved to a file 
        elif next_text == '-2':
            text_ui = {
                "text": "Mysterious Voice: You are defintley not the chosen one..(You dropped to the ground unconscious) GAME OVER!",
                "choices": [
                    {
                        'text': 'Restart Game',
                        'next_text': 0
                    }
                ]
            }
            return JsonResponse(text_ui)
        
        elif next_text == '-3':
            text_ui = {
                "text": "Really?...Like you forreal tried to fight a Druid...in the forest?...(You lost the battle - It wasnt even close) GAME OVER!",
                "choices": [
                    {
                        'text': 'Restart Game',
                        'next_text': 0
                    }
                ]
            }
            return JsonResponse(text_ui)        
        
        
        elif next_text == '-4':
            text_ui = {
                "text": "You join the Dark Wizards army and live but you really lost at heart - GAME OVER!",
                "choices": [
                    {
                        'text': 'Restart Game',
                        'next_text': 0
                    }
                ]
            }
            return JsonResponse(text_ui)         
    
        else:
            return JsonResponse( {"message": "Sorry, the game is not yet finished." } )




        
    else:
        return HttpResponseNotAllowed()   # No get requests, only POST, since these requests may affect the state of the data stored on the server. 
