from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from bookapp.models import StatusChoice


class GuestForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="Имя")
    email = forms.CharField(max_length=50, required=True, label="Email")
    text = forms.CharField(max_length=3000, label="Текст",
                           widget=widgets.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError('Имя должно быть длиннее 3 символов!')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise ValidationError("Email должен содержать '@'!")
        return email


class SearchForm(forms.Form):
    search = forms.CharField(
        label="поиск",
        max_length=300,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form mt-3', 'style': 'max-width: 300px; margin-left: 450px;'})
    )
