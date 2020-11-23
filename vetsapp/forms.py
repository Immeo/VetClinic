from .models import application
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class applicationForm(ModelForm):
    """
    docstring
    """
    class Meta:
        model = application
        fields = '__all__'
        
