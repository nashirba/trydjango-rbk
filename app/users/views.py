from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy

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
    context = {'photos': Photo.objects.filter(users=request.user)}
    return render(request, 'users/profile.html', context)


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('profile')

