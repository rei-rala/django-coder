from django.forms import ModelForm, TextInput, DateInput, NumberInput
from MVT.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'born': 'Fecha de nacimiento',
            'favourite_number': 'Número favorito',
            'relationship': 'Relación',
        }
        help_texts = {
            'name': 'Nombre de la persona',
            'born': 'Fecha de nacimiento',
            'favourite_number': 'Número favorito',
            'relationship': 'Relación',
        }
        error_messages = {
            'name': {
                'required': 'El nombre es obligatorio',
                'max_length': 'El nombre no puede tener más de 50 caracteres',
            },
            'born': {
                'required': 'La fecha de nacimiento es obligatoria',
            },
            'favourite_number': {
                'required': 'El número favorito es obligatorio',
                'max_value': 'El número favorito no puede ser mayor a 100',
                'min_value': 'El número favorito no puede ser menor a 0',
            },
            'relationship': {
                'required': 'La relación es obligatoria',
            },
        }
        widgets = {
            'name': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'born': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'favourite_number': NumberInput(attrs={'type': 'number', 'class': 'form-control'}),
            'relationship': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }