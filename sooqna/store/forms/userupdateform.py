from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms


class UserUpdateForm(UserChangeForm):


    class Meta:
        model = User
        fields = ('email', 'first_name', 'username')

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'