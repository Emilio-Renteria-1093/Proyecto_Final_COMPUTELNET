from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100 )
    password=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.email
