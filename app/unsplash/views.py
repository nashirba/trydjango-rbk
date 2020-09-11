import requests
from django.shortcuts import render
from django.conf import settings

BASE_URL = 'https://api.unsplash.com/'

def get_request():
    url = f'{BASE_URL}/photos/random'
    params = {
        'count':'10',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    request_content = requests.get(url, params=params)
    request_content = request_content.json()

    return request_content


def index_view(request):
    request_json = get_request()
    return render(request, 'index.html', {'request_json':request_json})


def search_view(request):
    return render(request, 'search.html')
