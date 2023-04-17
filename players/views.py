from django.shortcuts import render

from players.models import *


def list_players(request):
    template = 'players/list.html'
    players = Player.objects.select_related(
        'team').all()

    if 'country' in request.GET:
        # players = players.filter(country=request.GET['country'])
        country = request.GET['country']
        players = players.filter(country__iexact=country)

    context = {
        'players': players,
    }

    return render(request, template, context)
