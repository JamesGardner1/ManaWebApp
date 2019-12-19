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

    travlerUnderRock = True
  
    if request.method == 'POST':

        # TODO update user's game progress, as stored in the database 

        request_data = json.loads(request.body)
        next_text = request_data.get('next_text')

        print(request_data,next_text)

        if next_text == '0':
            jsonData = choices.get_next_choice(0)
            return JsonResponse(jsonData)
        
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

        elif next_text == '11':
            jsonData = choices.get_next_choice(11)
            return JsonResponse(jsonData)
        
        elif next_text == '12':
            jsonData = choices.get_next_choice(12)
            return JsonResponse(jsonData)        
        
        elif next_text == '13':
            jsonData = choices.get_next_choice(13)
            return JsonResponse(jsonData)

        elif next_text == '14':
            jsonData = choices.get_next_choice(14)
            return JsonResponse(jsonData)

        elif next_text == '15':
            jsonData = choices.get_next_choice(15)
            return JsonResponse(jsonData)

        elif next_text == '16':
            travelerUnderRock = False
            jsonData = choices.get_next_choice(16)
            return JsonResponse(jsonData)
        
        elif next_text == '17':
            jsonData = choices.get_next_choice(17)
            return JsonResponse(jsonData)
        
        elif next_text == '18':
            if (travelerUnderRock == False):
                jsonData = choices.get_next_choice(18)
                return JsonResponse(jsonData)
            else:
                text_ui = {
                    "id": 18,
                    "text": "(You descend farther ino the woods. You spot a lion walking towards you\nThe lion shifts into a man with tribal tattoos all over his body)\nDruid: Hello, human. I am a druid, a protector of the woods and all life that inhabit it. The forest observed you help that traveler back there. The forest rewards you.\n (Druid hands you over a scroll. You are rewarded with 15 experience points and a Healing Spell.)",
                    "choices": [
                        {
                            "text": ">>>",
                            "next_text": 21     
                        }
                    ]
                }
                return JsonResponse(text_ui)
        
        elif next_text == '19':
            jsonData = choices.get_next_choice(19)
            return JsonResponse(jsonData)
        
        elif next_text == '20':
            jsonData = choices.get_next_choice(20)
            return JsonResponse(jsonData)
        
        elif next_text == '21':
            jsonData = choices.get_next_choice(21)
            return JsonResponse(jsonData)
        
        elif next_text == '22':
            jsonData = choices.get_next_choice(22)
            return JsonResponse(jsonData)
        
        elif next_text == '23':
            jsonData = choices.get_next_choice(23)
            return JsonResponse(jsonData)
        
        elif next_text == '24':
            jsonData = choices.get_next_choice(24)
            return JsonResponse(jsonData)
        
        elif next_text == '25':
            jsonData = choices.get_next_choice(25)
            return JsonResponse(jsonData)
        
        elif next_text == '26':
            jsonData = choices.get_next_choice(26)
            return JsonResponse(jsonData)
        
        elif next_text == '27':
            jsonData = choices.get_next_choice(27)
            return JsonResponse(jsonData)
        
        elif next_text == '28':
            jsonData = choices.get_next_choice(28)
            return JsonResponse(jsonData)
        
        elif next_text == '29':
            jsonData = choices.get_next_choice(29)
            return JsonResponse(jsonData)
        
        elif next_text == '30':
            jsonData = choices.get_next_choice(30)
            return JsonResponse(jsonData)
        
        elif next_text == '31':
            jsonData = choices.get_next_choice(31)
            return JsonResponse(jsonData)
        
        elif next_text == '32':
            jsonData = choices.get_next_choice(32)
            return JsonResponse(jsonData)
        
        elif next_text == '33':
            jsonData = choices.get_next_choice(33)
            return JsonResponse(jsonData)
        
        elif next_text == '34':
            jsonData = choices.get_next_choice(34)
            return JsonResponse(jsonData)
        
        elif next_text == '35':
            jsonData = choices.get_next_choice(35)
            return JsonResponse(jsonData)
        
        elif next_text == '36':
            jsonData = choices.get_next_choice(36)
            return JsonResponse(jsonData)
        
        elif next_text == '37':
            jsonData = choices.get_next_choice(37)
            return JsonResponse(jsonData)
        
        elif next_text == '38':
            jsonData = choices.get_next_choice(38)
            return JsonResponse(jsonData)
        
        elif next_text == '39':
            jsonData = choices.get_next_choice(39)
            return JsonResponse(jsonData)
        
        elif next_text == '40':
            jsonData = choices.get_next_choice(40)
            return JsonResponse(jsonData)
        
        elif next_text == '41':
            jsonData = choices.get_next_choice(41)
            return JsonResponse(jsonData)

        elif next_text == '42':
            jsonData = choices.get_next_choice(42)
            return JsonResponse(jsonData)
        
        elif next_text == '43':
            jsonData = choices.get_next_choice(43)
            return JsonResponse(jsonData)
        
        elif next_text == '44':
            jsonData = choices.get_next_choice(44)
            return JsonResponse(jsonData)

        elif next_text == '45':
            jsonData = choices.get_next_choice(45)
            return JsonResponse(jsonData)

        elif next_text == '46':
            jsonData = choices.get_next_choice(46)
            return JsonResponse(jsonData)

        elif next_text == '47':
            jsonData = choices.get_next_choice(47)
            return JsonResponse(jsonData)
    
        elif next_text == '48':
            jsonData = choices.get_next_choice(48)
            return JsonResponse(jsonData)




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
                
    
        else:
            return JsonResponse( {"message": "Sorry, the game is not yet finished." } )




        
    else:
        return HttpResponseNotAllowed()   # No get requests, only POST, since these requests may affect the state of the data stored on the server. 