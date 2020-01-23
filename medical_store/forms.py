from django import forms


class ContactForm(forms.Form):
    fullname    = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email       = forms.EmailField()
    content     = forms.CharField()



class LoginForm(forms.Form):
    username    = forms.CharField()
    password    = forms.CharField()



class RegisterForm(forms.Form):
    username    = forms.CharField()
    email       = forms.EmailField()
    password    = forms.CharField(widget=forms.PasswordInput)
    password2   = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')