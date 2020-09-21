import requests

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .forms import SearchPhoto
from .models import Photo


BASE_URL = 'https://api.unsplash.com/'


def get_photos_url():
    url = f'{BASE_URL}/photos/random'
    params = {
        'count':'12',
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    response = response.json()
    return response


def search_photo_url(search_data):
    url = f'{BASE_URL}search/photos'
    params = {
        'query':search_data,
        'client_id':settings.UNSPLASH_ACCESS_KEY,
        'per_page' : 12
    }
    response = requests.get(url, params=params)
    response = response.json()
    return response


def detail_photo_url(id_photo):
    url = f'{BASE_URL}/photos/{id_photo}'
    params = {
        'client_id':settings.UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    response = response.json()
    return response


def save_photo(response, request):
    if request.user.is_authenticated:
        author = response['user']['name']
        image = response['urls']['small']
        photo_unsplash_id = response['id']
        if response['description']:
            description = response['description']
        else:
            description = response['alt_description']
        photo_data = {
            'author': author,
            'image': image,
            'description': description,
            'photo_unsplash_id': photo_unsplash_id
        }
        if Photo.objects.filter(photo_unsplash_id=photo_unsplash_id).exists():
            return messages.warning(request, 'photo already exists')
        photo_object= Photo.objects.create(**photo_data)
        photo_object.users.add(request.user)
        return messages.success(request, 'Photo is saved!')
    else:
        return messages.warning(request, 'You must be logged in to save!')


def index_view(request):
    search_form = SearchPhoto()
    if request.method == 'GET':
        search_form = SearchPhoto(request.GET)
    if request.method == 'POST': # save button
        response = response[photo_number]
        save_photo(response, request)
    response = get_photos_url()
    context = {
        'response': response,
        'search_form': search_form
    }
    return render(request, 'index.html', context)


def search_view(request):
    search_form = SearchPhoto()
    if request.method == 'GET':
        search_form = SearchPhoto(request.GET)
    else:
        search_form = ''
    response = get_photos_url()

    search_value = request.GET.get('query', None)
    response = search_photo_url(search_value)
    context = {
        'response': response,
        'search_form': search_form
    }
    return render(request, 'search.html', context)


def detail_view(request, id):
    response = detail_photo_url(id)
    context = {
        'response': response
    }
    if request.method == 'POST': # save button
        save_photo(response, request)
    return render(request, 'detail.html', context)


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('profile')
