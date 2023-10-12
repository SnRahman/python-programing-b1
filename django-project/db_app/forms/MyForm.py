from django import forms

class StudentForm(forms.Form):
    f_name = forms.CharField(max_length=100)
    l_name = forms.CharField(max_length=100)
    email = forms.EmailField()