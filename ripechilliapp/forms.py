from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter your Name'}), max_length=100)
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter your eMail'}), max_length=100)
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter your Phone Number'}), max_length=100)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':4,'cols':15,'placeholder': 'Enter your Message'}), max_length=500)
