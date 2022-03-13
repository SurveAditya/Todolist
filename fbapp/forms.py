from django import forms
from .models import EnModel

class EnForm(forms.Form):
	name=forms.CharField(label="Name")
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact'}))
	enq_msg=forms.CharField(widget=forms.Textarea(attrs={"rows":8,"cols":22,"style":"resize:none;"}))