from django.urls import path
from .views import index_view, search_view


urlpatterns = [
    path('', index_view, name='index'),
    path('search/', search_view, name='search')
]
