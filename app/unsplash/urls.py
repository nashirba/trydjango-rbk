from django.urls import path, include
from .views import index_view


urlpatterns = [
    path('', index_view, name='index')
]
