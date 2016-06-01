# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import foursquare
from django.conf import settings
from pprint import pprint
import random

# Create your views here.

@require_http_methods(["POST",])
@csrf_exempt
def lunch(request):

    '''
    token=SLACK_KEY
    team_id=T0001
    team_domain=example
    channel_id=C2147483705
    channel_name=test
    user_id=U2147483697
    user_name=Steve
    command=/weather
    text=94070
    response_url=https://hooks.slack.com/commands/1234/5678
    '''
    client = foursquare.Foursquare(client_id=settings.FS_CLIENT_ID, client_secret=settings.FS_CLIENT_SECRET)
    token = request.POST.get('token')

    venues = client.venues.explore(params={
    'll': '39.1015337,-84.5173639',
    'radius': '1750',
    'section': 'food',
    'price': '1,2',
    'openNow': '1'})

#    pprint(venue)

    places = []
    recs = " \n"

    for groups in venues['groups']:
        for items in groups['items']:
            places.append(items['venue']['name'])

    choices = random.sample(places, 5)

# menu url

    for index, item in enumerate(choices):
        if index == 0: emoji = ":one: "
        if index == 1: emoji = ":two: "
        if index == 2: emoji = ":three: "
        if index == 3: emoji = ":four: "
        if index == 4: emoji = ":five: "
        recs += '%s %s \n' % (emoji, item)

    return JsonResponse({"response_type": "in_channel", "text": recs})
