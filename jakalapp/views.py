from django.shortcuts import render

# Create your views here.

from jakalapp.models import Player

import random

fields  = Player._meta.fields[1:]
players = Player.objects.all()
correct_index = random.randint(1, players.count())
correct_player = {"player" : players.get(id=correct_index)}
green = "green"
yellow = "yellow"
guessed_players = []
num_guesses = 5

def show_jakal(request):
    over = False
    guess_hints = setHints()
    if (num_guesses == len(guessed_players)):
        over = True
    if (request.method == "GET"):
        guessed_players.clear()
        correct_index = random.randint(1, players.count())
        correct_player["player"] = players.get(id=correct_index)
    if (request.method == "POST"):
        guessed_player = players.get(id=request.POST.get("guessed_player"))
        if (guessed_player == correct_player["player"]):
            over = True
        guess_hints = getHints(guessed_player)
        guess = {"hints" : guess_hints, "player" : guessed_player}
        if (not guessed_players.__contains__(guess)):
            guessed_players.append(guess)

    available_players = players
    available_players = [p for p in available_players if p not in guessed_players]
    return render(request, "main.html", 
                  {"fields" : fields, "players" : available_players, 
                   "guessed_players" : guessed_players, "over" : over, "num_guesses" : num_guesses - len(guessed_players)})

def setHints():
    hints = {}
    hints["name"] = "gray"
    hints["country"] = "gray"
    hints["rank"] = "gray"
    hints["main"] = "gray"
    hints["team"] = "gray"
    return hints

def getHints(player):
    hints = {}
    rankHints(hints, player)
    countryHints(hints, player)
    mainHints(hints, player)
    if (player.name == correct_player["player"].name):
        hints["name"] = green
    if (player.team == correct_player["player"].team):
        hints["team"] = green
    return hints

def rankHints(hints, player):
    if (player.rank == correct_player["player"].rank):
        hints["rank"] = green
    elif (abs(player.rank - correct_player["player"].rank) <= 2):
        hints["rank"] = yellow

def countryHints(hints, player):
    if (player.country == correct_player["player"].country):
        hints["country"] = green
    elif (player.country.continent == correct_player["player"].country.continent):
        hints["country"] = yellow

def mainHints(hints, player):
     if (player.main == correct_player["player"].main):
        hints["main"] = green
     elif (player.main == correct_player["player"].main.franchise):
         hints["main"] = yellow

