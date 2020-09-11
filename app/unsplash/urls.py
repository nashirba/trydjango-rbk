from django.urls import path, include
from .views import view_index


urlpatterns = [
    path('', view_index, name='index')
]
