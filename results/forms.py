#-*- coding: utf-8 -*-
from django import forms
from .models import Pointing

class PointingForm(forms.ModelForm):
    class Meta:
        model = Pointing
        fields = '__all__'

class JoinForm(forms.Form):
    n_grilles = forms.FloatField(label='On te prépare combien de grilles ?', min_value=1, max_value=100)
