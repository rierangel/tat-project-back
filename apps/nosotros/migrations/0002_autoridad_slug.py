# Generated by Django 4.1.2 on 2022-11-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoridad',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
