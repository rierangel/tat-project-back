# Generated by Django 4.1.2 on 2022-11-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marco_normativo', '0003_rename_edictos_acuerdo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acuerdo',
            name='archivo',
            field=models.FileField(upload_to='marco-normativo/acuerdos'),
        ),
        migrations.AlterField(
            model_name='convenio',
            name='archivo',
            field=models.FileField(upload_to='marco-normativo/convenios'),
        ),
        migrations.AlterField(
            model_name='edicto',
            name='archivo',
            field=models.FileField(upload_to='marco-normativo/edictos'),
        ),
        migrations.AlterField(
            model_name='flujograma',
            name='archivo',
            field=models.FileField(upload_to='marco-normativo/flujograma'),
        ),
        migrations.AlterField(
            model_name='leyesydecreto',
            name='archivo',
            field=models.FileField(upload_to='marco-normativo/leyes-y-decretos'),
        ),
    ]
