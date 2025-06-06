from django.db import models


# Create your models here.
class usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    senha = models.CharField(max_length=128)

    ADMINISTRADOR = 'administrador'
    USUARIO = 'usuario'
    PROGRAMADOR = 'programador'
    CARGO_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (USUARIO, 'Usuario'),
        (PROGRAMADOR, 'Programador')
    ]
    cargo = models.CharField(max_length=15, choices=CARGO_CHOICES, default=USUARIO)
    def __str__(self):
        return self.nome