from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import UserRegisterForm
from app.unsplash.models import Photo


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    object_list = Photo.objects.filter(users=request.user)  
    paginator = Paginator(object_list, 3)  # 3 фоток на каждой странице  
    page = request.GET.get('page')  
    try:  
        photos = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        photos = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        photos = paginator.page(paginator.num_pages)  
    context = {
        'page': page,
        'photos': photos,
        }
    return render(request, 'users/profile.html', context)
