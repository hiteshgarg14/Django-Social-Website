from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

"""
Django also provides a UserCreationForm form that you can use, which resides in
django.contrib.auth.forms and is very similar to the one we have created
"""
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    """
    This check is done when we validate the form calling its is_valid() method.
    You can provide a clean_<fieldname>() method to any of your form fields in
    order to clean the value or raise form validation errors for the specific field.
    """
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError('Password don\'t match.')
        return cd["password2"]
