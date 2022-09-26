from django.forms import ModelForm, TextInput, Textarea
from .models import English


class FormEnglish(ModelForm):
    class Meta:
        model = English
        fields = ['name', 'text']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Введите заголовок для вашего (правила, слова, времена)",
                'class': 'form-control',
            }),
            'text': Textarea(attrs={
                'placeholder': "Описание",
                'class': 'form-control',
            })
        }

