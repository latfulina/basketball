from .models import Record
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea



class RecordForm (ModelForm):
    class Meta:
        model = Record
        fields = ['title','level', 'full_text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            'level': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уровень подготовки'
            }),
            'full_text':DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата для записи на тренировку'

            }),

        }