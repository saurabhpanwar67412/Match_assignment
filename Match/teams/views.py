from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random

# Create your views here.

def home(request):

    team = Team.objects.all()
    return render(request, 'teams/index.html', {'team' : team })

def players(request):
    id=request.POST.get('submit')
    players = Player.objects.filter(team=id)
    return render(request, 'players/players.html', {'players':  players })


def match(request):
    matches = Matches.objects.all()
    return render(request, 'matches/match.html', {'matches' : matches })

def points(request):
    points = Points.objects.all()
    return render(request, 'points/point.html', {'points' : points })

def matchfix(request): 
    if request.method == 'POST':
        team1 = request.POST.get('team1')
        team2 = request.POST.get('team2')
        winner = random.choice([team1, team2])
        obj = Matches() 
        obj.matchesBetweenteams = team1 + " & " + team2
        obj.Winner = winner
        obj.save()   

        obj = Points() 
        obj.teampoints = winner
        obj.points +=1 
        obj.save() 
    return HttpResponse( "Winner of the match is " + winner)

        

