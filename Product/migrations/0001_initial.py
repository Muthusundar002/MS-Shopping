# Generated by Django 4.2.15 on 2024-08-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('Price', models.IntegerField(default=0)),
                ('GST', models.FloatField(default=0)),
                ('Final_price', models.IntegerField(default=0)),
            ],
        ),
    ]
