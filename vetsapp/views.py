from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from .models import application
from .forms import applicationForm
# from django.contrib.auth.forms import Customer/
from django.contrib import messages
#  Create your views here.


def index(request):
    """
    main page
    """
    return render(request, 'vetsapp/index.html')

@login_required
def record(request):
    """
    record view
    """
    bag = ''

    if request.method == 'POST':
        form = applicationForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.user = form.cleaned_data.get('user_nickname')
            print(content.user)
            content.save()
            messages.success(request, 'Вы успешно подали заявку')
            # return redirect('')
        else:
            bag = 'Вы ввели неверные данные'
            print(form)
        print(form)
    form = applicationForm()

    data = {
        'form': form,
        'bag': bag
    }
    
    return render(request, 'vetsapp/record.html', data)


@login_required
def profile_user(request):
    """
    profile users
    """
    content = {
        'application': application.objects.filter(user_nickname=request.user)
    }
    Template = 'account/profile.html'
    return render(request, Template, content)
