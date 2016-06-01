from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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

    token = request.POST.get('token')
    text = 'temp'
    return HttpResponse(token)
