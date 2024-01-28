from .models import Links
from django.forms import ModelForm, TextInput, DateTimeInput


class LinksForm(ModelForm):
    class Meta:
        model = Links
        fields = ['url', 'alias', 'date']

        widgets = {
            'url': TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Введите ссылку'
            }),

            'alias': TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Введите алиас'
            }),
            'date': DateTimeInput   (attrs={
                "class": 'form-control',
                'placeholder': 'Введите дату'
            }),
        }


class GetUrl(ModelForm):
    class Meta:
        model = Links
        fields = ['alias']

        widgets = {
            'alias': TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Введите alias'
            })
        }

