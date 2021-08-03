from django import forms
from django.core.exceptions import ValidationError

from phonebook.models import Phboo


class PhbooForm(forms.ModelForm):

    class Meta:
        model = Phboo
        fields = ['name', 'nomer', 'birthday', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'nomer': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_url(self):
        new_url = self.cleaned_data['url'].lower()

        if new_url == 'create':
            raise ValidationError('Url не может быть создан')
        return new_url