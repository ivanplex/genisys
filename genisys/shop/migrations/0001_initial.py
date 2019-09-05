# Generated by Django 2.2.4 on 2019-09-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtomicComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock_code', models.CharField(max_length=255)),
                ('part_code', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('warehouse_location', models.IntegerField(blank=True, null=True)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=1000, null=True)),
                ('availability', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
