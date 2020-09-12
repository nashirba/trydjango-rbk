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


def search_photo(search_data):
    url = f'{BASE_URL}search/photos'
    params = {
        'query':search_data,
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    request_content = requests.get(url, params=params)
    request_content = request_content.json()
    return request_content


def detail_photo(id_photo):
    url = f'{BASE_URL}/photos/:{id_photo}'
    request_content = requests.get(url)
    request_content = request_content.json()
    return request_content


def index_view(request):
    search_form = SearchPhoto()
    if request.method == 'GET':
        search_form = SearchPhoto(request.GET)
    request_json = get_photos()
    context = {
        'request_json': request_json,
        'search_form': search_form
    }
    return render(request, 'index.html', context)


def search_view(request):
    search_value = request.GET.__getitem__('Search')
    search_json = search_photo(search_value)
    context = {
        'search_json': search_json
    }
    return render(request, 'search.html', context)


def detail_view(request, id):
    detail_json = detail_photo(id)
    context = {
        'detail_json': detail_json
    }
    return render(request, 'detail.html', context)