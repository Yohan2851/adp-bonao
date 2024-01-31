from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from django.views import View



from .forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.
# def home_view(request):
#     user = request.user
#     admin_link = reverse('admin:index')
#     return render(request, 'index.html',{'admin_link': admin_link})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
    else:
        login_form = CustomAuthenticationForm()
    return render(request, 'logaut/login.html', {'form': login_form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creatio_form = CustomUserCreationForm(data=request.POST)
        if user_creatio_form.is_valid():
            user_creatio_form.save()
            user = authenticate(
                username=user_creatio_form.cleaned_data['username'],
                password=user_creatio_form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')

    return render(request, 'logaut/register.html', {
        'form': CustomUserCreationForm()
    })

@login_required
def custom_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    user = request.user
    user_actions = LogEntry.objects.filter(user=request.user)
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'picture': user.picture.url,
        'user_actions': user_actions

    }
    return render(request, 'profile.html', context)