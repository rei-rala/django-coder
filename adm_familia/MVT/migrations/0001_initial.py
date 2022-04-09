# Generated by Django 4.0.3 on 2022-04-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('born', models.DateField()),
                ('favourite_number', models.IntegerField()),
                ('relationship', models.CharField(default='Desconocido', max_length=30)),
            ],
        ),
    ]
