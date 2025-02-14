from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Jelszó", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Jelszó újra", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("A két jelszó nem egyezik!")
        return self.cleaned_data["password2"]
