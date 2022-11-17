# Generated by Django 4.1.2 on 2022-11-10 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasResoluciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Resolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('año', models.IntegerField(default=2020)),
                ('archivo', models.FileField(upload_to='uploads/resoluciones/%Y/%m/%d/')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resolucion', to='publicaciones.categoriasresoluciones')),
            ],
        ),
    ]
