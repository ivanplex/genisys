# Generated by Django 2.2.4 on 2019-09-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190903_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atomicrequirement',
            old_name='quantity',
            new_name='max_quantity',
        ),
        migrations.RenameField(
            model_name='blueprintrequirement',
            old_name='quantity',
            new_name='max_quantity',
        ),
        migrations.AddField(
            model_name='atomicrequirement',
            name='min_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='blueprintrequirement',
            name='min_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
