# Generated by Django 4.2.15 on 2024-09-11 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='Username',
        ),
    ]
