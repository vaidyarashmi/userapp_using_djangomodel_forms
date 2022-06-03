from dataclasses import field
from django import forms
from testapp.models import User
from django.core.exceptions import ValidationError
import re
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

    def clean_email(self):
        email_from_dict=self.cleaned_data['email']
        if User.objects.filter(email=email_from_dict).exists():
            raise ValidationError("Email already exists. Please specify another email id ")
        return email_from_dict
    
    def clean_first_name(self):
        first_name_from_dict=self.cleaned_data['first_name']
        if not re.match("^[A-Za-z]*$", first_name_from_dict):
            raise ValidationError("please enter only string in first name")
        return first_name_from_dict
    
    def clean_last_name(self):
        last_name_from_dict=self.cleaned_data['last_name']
        if not re.match("^[A-Za-z]*$",last_name_from_dict):
            raise ValidationError('Please enter only string in last name ')
        return last_name_from_dict
        