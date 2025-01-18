from django.contrib.auth.models import User
from django.db import models
from datetime import date



class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to="autores/", blank=True, null=True)

    def __str__(self):
        return self.usuario.username


class Post(models.Model):

    titulo = models.CharField(max_length=30)
    conteudo = models.TextField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_criacao = models.DateField('Data de criação', default=date(year=1900, month=1, day=1))
    data_atualizacao = models.DateField('Data de atualização', default=date(year=1900, month=1, day=1))
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo