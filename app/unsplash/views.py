import requests
from django.shortcuts import render


def get_request():
    base_url = 'https://api.unsplash.com/'
    UNSPLASH_ACCESS_KEY = '-RbPPqlmBdwSR5Clv8dMs8oCLfrK7KvB3um-dp7-swY'
    request_content = requests.get(
        base_url + '/photos/random?count=2' + '&' + 'client_id=' + UNSPLASH_ACCESS_KEY
    )
    request_content = request_content.json()

    return request_content

def index_view(request):
    request_json = get_request()
    return render(request, 'index.html', {'request_json':request_json})
