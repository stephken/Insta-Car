# Generated by Django 3.1.2 on 2020-10-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('year', models.CharField(max_length=4)),
                ('color', models.CharField(max_length=30)),
                ('time_posted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
