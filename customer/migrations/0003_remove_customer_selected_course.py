# Generated by Django 4.2.15 on 2024-09-04 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_selected_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Selected_course',
        ),
    ]
