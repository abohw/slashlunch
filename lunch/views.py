from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
    venue = client.venues('40a55d80f964a52020f31ee3')
    something = venue['venue']['name']
    print something
#    pprint(venue)
    text = 'temp'
    return HttpResponse(token)
