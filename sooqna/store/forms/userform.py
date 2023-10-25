from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder': 'Email','class':'form-inputs'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'First Name','class':'form-inputs'}))

    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name')

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].widget.attrs['class'] = 'form-inputs'

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-inputs'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-inputs'



    