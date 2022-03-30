from django.db import models

class Persona(models.Model):
    name = models.CharField(max_length=50)
    born = models.DateField()
    favourite_number = models.IntegerField()
    relationship = models.CharField(max_length=30, default='Desconocido')
    
    def __str__(self) -> str:
        return f'Persona #{self.id}: {self.name} | Relación: ({self.relationship})'

# Alternativa a seguir:
# crear clase para "Familiar" con nuevos atributos