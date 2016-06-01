# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import foursquare
from django.conf import settings
from pprint import pprint

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
#    venue = client.venues('40a55d80f964a52020f31ee3')
    venues = client.venues.explore(params={'ll': '39.1015337,-84.5173639', 'limit': '5', 'openNow': '1'})

#    pprint(venue)

    places = []
    recs = ''

    for groups in venues['groups']:
        for items in groups['items']:
            places.append(items['venue']['name'])

    for index, item in enumerate(places):
        if index == 0: emoji = ":one:"
        if index == 1: emoji = ":two:"
        if index == 2: emoji = ":three:"
        if index == 3: emoji = ":four:"
        if index == 4: emoji = ":five:"
        recs += '%s %s \n' % (emoji, item)

# use user_name when actually in Slack

    return JsonResponse({"response_type": "in_channel", "text": recs})
