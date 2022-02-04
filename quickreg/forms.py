from dataclasses import fields
import imp
from django import forms
from .models import Emailtemplate, User

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model=User
        
        fields='__all__'

class mailregister(forms.ModelForm):
    class Meta :
        model = Emailtemplate

        fields='__all__'