from .models import Todo
from django.forms import ModelForm, TextInput, Textarea


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введіть назву'
                }),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введіть опис'
                }),
        }
