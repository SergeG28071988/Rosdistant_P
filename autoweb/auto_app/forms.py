from .models import Auto
from django.forms import ModelForm, TextInput


class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['brand', 'model', 'year', 'color']
        widgets = {
            "brand": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите бренд'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите модель'
            }),
            "year": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год'
            }),
            "color": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цвет'
            }),
        }
