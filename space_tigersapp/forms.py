from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User # <- model to base the form off of
        #fields to display in the form
        fields = ['first_name', 'middle_initial', 'last_name', 'email', 'phone', 'avatar_url']
