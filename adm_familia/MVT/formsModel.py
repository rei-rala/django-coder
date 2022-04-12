from django.forms import ModelForm, TextInput, DateInput, NumberInput
from MVT.models import Person, Movie, Brand

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'born': 'Fecha de nacimiento',
            'favourite_number': 'Número favorito',
        }
        help_texts = {
            'name': 'Nombre de la persona',
            'born': 'Fecha de nacimiento',
            'favourite_number': 'Número favorito',
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
        }
        widgets = {
            'name': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'born': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'favourite_number': NumberInput(attrs={'type': 'number', 'class': 'form-control'}),
        }
    

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            "title": "Título",
            'genre': 'Género',
        }
        help_texts = {
            'title': 'Título de la película',
            'genre': 'Género de la película',
        }
        error_messages = {
            'title': {
                'required': 'El título es obligatorio',
            },
            'genre': {
                'required': 'El género es obligatorio',
            }
        }
        widgets = {
            'title': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'genre': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }
        
class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        labels = {
            "name": 'Nombre de la marca',
            'segment': 'Segmento de la marca',
        }
        help_texts = {
            'name': 'Nombre de la marca',
            'segment': 'Segmento de la marca',
        }
        error_messages = {
            'name': {
                'required': 'El nombre es obligatorio',
            },
            'segment': {
                'required': 'El segmento es obligatorio',
            }
        }
        widgets = {
            'name': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'segment': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }