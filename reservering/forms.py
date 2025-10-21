
from django import forms
from .models import Reservering

class ReserveringForm(forms.ModelForm):
    class Meta:
        model = Reservering
        fields = ['naam', 'email', 'datum']

