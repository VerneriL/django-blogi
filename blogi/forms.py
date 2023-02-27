from django.forms import ModelForm
from .models import Postaus


class UusiPostausForm(ModelForm):
    class Meta:
        model = Postaus
    
    fields = ['otsikko', 'teksti']