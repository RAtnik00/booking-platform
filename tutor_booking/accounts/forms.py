from django import forms
from accounts.models import CustomUser
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=6,
        help_text="The password must be at least 6 characters long."
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'role']

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise ValidationError("The username cannot contain spaces.")
        if len(username) > 30:
            raise ValidationError("The username can have a maximum of 30 characters.")
        return username