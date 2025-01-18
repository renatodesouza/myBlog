from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Autor, Post


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'bio', 'foto_perfil')

    fieldsets = [
        ('Informações pessoais',            {'fields':('usuario', 'bio', 'foto_perfil')})
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'conteudo', 'autor', 'data_criacao', 'data_atualizacao', 'publicado')

    fieldsets = [
        ('Informações do POST',             {'fields':('titulo', 'autor')}),
        ('Conteudo',                        {'fields':('conteudo',)}),
        ('Data',                            {'fields':('data_criacao', 'data_atualizacao')}),
        ('Publicado',                       {'fields':('publicado',)}),

    ]

    