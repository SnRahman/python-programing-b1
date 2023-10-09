from django import forms

class StudentForm(forms.Form):
    
    first_name = forms.CharField(
        max_length=255,
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        error_messages= {'invalid':'Fist name is required'}
        )
    
    last_name = forms.CharField(
        max_length=255,
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        error_messages= {'invalid':'Last name is required'}
        )
    
    email = forms.EmailField(
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        error_messages= {'invalid':'invalid email format'}
        )