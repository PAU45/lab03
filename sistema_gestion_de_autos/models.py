from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    numero_apartamento = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Correo único

    def __str__(self):
        return self.nombre
    

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=15, unique=True)  # Matrícula única
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"
class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='registros')
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Registro de {self.vehiculo} - Entrada: {self.fecha_hora_entrada}"