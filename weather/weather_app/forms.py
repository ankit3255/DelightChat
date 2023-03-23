# forms.py

from django import forms
from .models import Location

class FavouriteLocationsForm(forms.ModelForm):
    locations = forms.ModelMultipleChoiceField(queryset=Location.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Profile
        fields = ['locations']
