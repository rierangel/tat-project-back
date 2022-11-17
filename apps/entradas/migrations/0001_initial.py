# Generated by Django 4.1.2 on 2022-11-10 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Congreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateField()),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen_principal', models.ImageField(upload_to='entradas/congreso')),
            ],
        ),
        migrations.CreateModel(
            name='HaciendoDiferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateField()),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen_principal', models.ImageField(upload_to='entradas/galeria_haciendo_diferencia')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateField()),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen_principal', models.ImageField(upload_to='entradas/noticias')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='entradas/noticias/galeria')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='entradas.noticia')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaHaciendoDiferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='entradas/galeria_haciendo_diferencia/galeria')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='entradas.haciendodiferencia')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaCongreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='entradas/congreso/galeria')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='entradas.congreso')),
            ],
        ),
    ]
