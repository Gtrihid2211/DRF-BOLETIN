from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    COCHE = 'COCHE'
    CICLOMOTOR = 'CICLOMOTOR'
    MOTOCICLETA = 'MOTOCICLETA'

    TIPO_CHOICES = [
        (COCHE, 'Coche'),
        (CICLOMOTOR, 'Ciclomotor'),
        (MOTOCICLETA, 'Motocicleta'),
    ]

    ROJO = 'ROJO'
    AZUL = 'AZUL'
    VERDE = 'VERDE'
    BLANCO = 'BLANCO'

    COLOR_CHOICES = [
        (ROJO, 'Rojo'),
        (AZUL, 'Azul'),
        (VERDE, 'Verde'),
        (BLANCO, 'Blanco'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    chasis = models.CharField(max_length=100, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    fecha_fabricacion = models.DateField()
    fecha_matriculacion = models.DateField()
    fecha_baja = models.DateField(null=True, blank=True)
    suspendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"

