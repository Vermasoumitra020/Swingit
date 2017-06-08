from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullname', 'email', 'bday']
