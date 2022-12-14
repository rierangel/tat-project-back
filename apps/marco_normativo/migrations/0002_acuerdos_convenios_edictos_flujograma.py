# Generated by Django 4.1.2 on 2022-11-13 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marco_normativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acuerdos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('año', models.IntegerField(choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='año')),
                ('archivo', models.FileField(max_length=500, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Convenios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('año', models.IntegerField(choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='año')),
                ('archivo', models.FileField(max_length=500, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Edictos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('año', models.IntegerField(choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='año')),
                ('archivo', models.FileField(max_length=500, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Flujograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('inicio', models.DateField(auto_now=True)),
                ('final', models.DateField(auto_now=True)),
                ('archivo', models.FileField(max_length=500, upload_to='')),
            ],
        ),
    ]
