from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import applicationForm
# , RegisterForm, UserLoginForm
from .models import application
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView
#  Create your views here.


def index(request):
    """
    main page
    """
    return render(request, 'vetsapp/index.html')


def profile_user(request):
    """
    docstring
    """
    content = {
        'application': application.objects.filter(user=request.usr)
    }
    return render(request, 'account/profile.html', content)


def record(request):
    """
    record view
    """
    bag = ''

    if request.method == 'POST':
        form = applicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно подали заявку')
            return redirect('home')
        else:
            bag = 'Вы ввели неверные данные'

    form = applicationForm()

    data = {
        'form': form,
        'bag': bag
    }
    return render(request, 'vetsapp/record.html', data)
