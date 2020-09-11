import requests
from django.shortcuts import render
from django.conf import settings
from .forms import SearchPhoto


BASE_URL = 'https://api.unsplash.com/'


def get_photos():
    url = f'{BASE_URL}/photos/random'
    params = {
        'count':'10',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    request_content = requests.get(url, params=params)
    request_content = request_content.json()

    return request_content

# delete this function later after creating form for search photo
# def search_photo():
#     url = f'{BASE_URL}search/photos'
#     params = {
#         'query':'#',
#         'client_id':settings.UNSPLASH_ACCESS_KEY
#     }
#     request_content = requests.get(url, params=params)
#     request_content = request_content.json()

#     return request_content


def index_view(request):
    request_json = get_photos()
    return render(request, 'index.html', {'request_json': request_json})


def search_view(request):
    if request.method == 'GET':
        search_form = SearchPhoto()
        print('----------------------------')
        print(search_form)
        print('----------------------------')
        url = f'{BASE_URL}search/photos'
        params = {
            'query':'#',
            'client_id':settings.UNSPLASH_ACCESS_KEY
        }
        request_content = requests.get(url, params=params)
        request_content = request_content.json()
    return render(request, 'search.html', {'search_form': search_form})
