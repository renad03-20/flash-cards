from django import forms
from .models import Card

class cardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['front_q', 'back_a']