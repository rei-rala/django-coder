from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


    

class Color(models.Model):
    red = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(255)])
    green = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(255)])
    blue = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(255)])
    
    def __str__(self) -> str:
        return f"Color #{self.id} - Red: {self.red} | Green: {self.green} | Blue {self.blue}"
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"Marca #{self.id}: {self.name}"
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    born = models.DateField()
    favourite_number = models.IntegerField()
    relationship = models.CharField(max_length=30, default="Desconocido")
    favourite_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    favourite_color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Persona #{self.id}: {self.name}"


# Alternativa a seguir:
"""
# Crear clase para "Familiar" con nuevos atributos

class Familiar(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=30, default='Desconocido')
    
    def __str__(self) -> str:
        return f'Familiar #{self.id}: {self.Person.name} | Relación: ({self.relationship})'
    
"""
