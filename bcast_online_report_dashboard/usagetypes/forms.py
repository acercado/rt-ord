from django import forms
from .models import Dashboard

class Dashboard(forms.ModelForm):

    class Meta:
        model = Dashboard
        fields = ('usagetype', 'daterange_start', 'daterange_end')
