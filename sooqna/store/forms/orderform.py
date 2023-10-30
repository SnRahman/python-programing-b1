from django import forms
from ..models import Order


class OrderForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # address = forms.CharField(max_length=500)
    # city = forms.CharField(max_length=100)
    # phone = forms.CharField(max_length=15)

    class Meta:
        model = Order
        fields = ('__all__')
        exclude = ('user', 'order_amount', 'payment_mode')

    
    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['last_name'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['address'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['city'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['phone'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['email'].widget.attrs['class'] = 'form-control nav-search'


    
