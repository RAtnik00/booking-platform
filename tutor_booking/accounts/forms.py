from django import forms
from accounts.models import CustomUser, TutorProfile
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=6,
        help_text="The password must be at least 6 characters long.",
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

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded shadow focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }

class TutorProfileForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded shadow focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    class Meta:
        model = TutorProfile
        fields = ['bio', 'experience_years', 'subjects', 'price_per_hour']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded shadow focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 4
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded shadow focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'subjects': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded shadow focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'price_per_hour': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded shadow focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = user.username

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            profile.save()
        return profile

