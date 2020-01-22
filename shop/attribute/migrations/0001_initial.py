# Generated by Django 2.2.6 on 2020-01-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('visibility', models.CharField(blank=True, choices=[('online', 'online'), ('inherit', 'inherit')], max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
