# Generated by Django 2.2.6 on 2019-10-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atomic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atomicprerequisite',
            name='virtual',
            field=models.BooleanField(default=False),
        ),
    ]
