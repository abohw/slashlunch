from __future__ import unicode_literals

from django.apps import AppConfig


class LunchConfig(AppConfig):
    name = 'lunch'

@app.route('/lunch', methods=['post'])
def lunch():
    text = 'temp'
    return text
