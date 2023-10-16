from django import forms
from .models import HarAnalysis

class HarAnalysisForm(forms.ModelForm):
    class Meta:
        model = HarAnalysis
        fields = ['har_file']