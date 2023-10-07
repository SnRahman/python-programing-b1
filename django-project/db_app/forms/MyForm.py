from django import forms

class StudentForm(forms.Form):
    f_name = forms.CharField(max_length=100,label='First Name')
    l_name = forms.CharField(max_length=100,label='Last Name')
    email = forms.EmailField(label='Email')