from django import forms
from .models import Order

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    address1 = forms.CharField(label='Address Line 1', max_length=100)
    address2 = forms.CharField(label='Address Line 2', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    state = forms.CharField(label='State', max_length=100)
    country = forms.CharField(label='Country', max_length=100)
    order_note = forms.CharField(label='Order Note', max_length=100)
    
