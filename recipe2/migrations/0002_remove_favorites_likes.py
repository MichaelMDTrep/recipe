# Generated by Django 3.1.4 on 2020-12-12 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='likes',
        ),
    ]
