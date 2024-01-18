# from django.shortcuts import render
# Create your views here.

n = 3
cards = {'commander': n, 'princess': n, 'assassin': n,
         'nobleman': n, 'ambassador': n, 'inspector': n}


def normal_game(request):
    from game.models import NormalGame
    game = NormalGame(request)      # need alot of change at this level
    if game.is_start:
        game.card_storage = cards


"""def assassin(x):
    target = 'kazem'
    if target == cards['princess']:
        print(cards['princess'])
        print("your safe baby")
    else:
        print(cards['princess'])
        print('shine baaka')"""

# first we need to make a shuffle system
