# Generated by Django 4.2 on 2025-01-18 13:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='autores/')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('conteudo', models.CharField(max_length=100)),
                ('data_criacao', models.DateField(default=datetime.date(1900, 1, 1), verbose_name='Data de criação')),
                ('data_atualizacao', models.DateField(default=datetime.date(1900, 1, 1), verbose_name='Data de atualização')),
                ('publicado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
            ],
        ),
    ]
