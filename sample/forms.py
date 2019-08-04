from django import forms
from django.conf import settings

class LanguageForm(forms.Form):
    code = forms.ChoiceField(choices=settings.LANGUAGES)
