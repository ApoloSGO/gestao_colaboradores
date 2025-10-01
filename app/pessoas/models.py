from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username

class Documento(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
