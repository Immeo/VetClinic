from django.urls import path
from django.conf.urls.static import static
from allauth.account.views import LoginView, SignupForm
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('record', views.record, name='record'),
    path('profile', views.profile_user, name='profile'),
]
