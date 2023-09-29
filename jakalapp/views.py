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
guesses = []
num_guesses = 5

# Handles showing the contents of the Jakalapp page
def show_jakal(request):
    over = False
    guess_hints = setHints("gray")

    if (request.method == "GET"):
        guesses.clear()
        correct_index = random.randint(1, players.count())
        correct_player["player"] = players.get(id=correct_index)
        over = False

    if (request.method == "POST"):
        guessed_player = players.get(id=request.POST.get("guessed_player"))
        if (guessed_player == correct_player["player"]):
            over = True
        guess_hints = getHints(guessed_player)
        guess = {"hints" : guess_hints, "player" : guessed_player}
        if (not guesses.__contains__(guess)):
            guesses.append(guess)

    if (num_guesses == len(guesses)):
        over = True
        wrong_hints = setHints("red")
        guess = {"hints" : wrong_hints, "player" : correct_player['player']}
        guesses.append(guess)

    available_players = get_available()
    guesses_left = 0 if num_guesses - len(guesses) < 0 else num_guesses - len(guesses) 
    return render(request, "main.html", 
                  {"fields" : fields, "players" : available_players, 
                   "guessed_players" : guesses, "over" : over, "num_guesses" : guesses_left})

# Adds the available players left to guess
def get_available():
    guessed_players = []
    for guess in guesses:
        guessed_players.append(guess["player"])
    available = [p for p in players if p not in guessed_players]
    return available

# Sets the hint dictionary to a given color
def setHints(color):
    hints = {}
    hints["name"] = color
    hints["country"] = color
    hints["rank"] = color
    hints["main"] = color
    hints["team"] = color
    return hints

# Gets the corresponding hints from a guessed player
def getHints(player):
    hints = {}
    rank_hints(hints, player)
    country_hints(hints, player)
    main_hints(hints, player)
    if (player.name == correct_player["player"].name):
        hints["name"] = green
    if (player.team == correct_player["player"].team):
        hints["team"] = green
    return hints

# Gets the corresponding rank hints from a guessed player
def rank_hints(hints, player):
    if (player.rank == correct_player["player"].rank):
        hints["rank"] = green
    elif (abs(player.rank - correct_player["player"].rank) <= 2):
        hints["rank"] = yellow

# Gets the corresponding country hints from a guessed player
def country_hints(hints, player):
    if (player.country == correct_player["player"].country):
        hints["country"] = green
    elif (player.country.continent == correct_player["player"].country.continent):
        hints["country"] = yellow

# Gets the corresponding main hints from a guessed player
def main_hints(hints, player):
     if (player.main == correct_player["player"].main):
        hints["main"] = green
     elif (player.main == correct_player["player"].main.franchise):
         hints["main"] = yellow

# Renders the template for showing how to play Jakal
def show_how_to_play(request):
    return render(request, "play.html")