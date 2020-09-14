from django.contrib import admin
from django.urls import path, include
from app.users import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('', include('app.unsplash.urls'))
]
