# Generated by Django 4.1.6 on 2023-03-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0003_postaus_kuva'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaus',
            name='ingressi',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
