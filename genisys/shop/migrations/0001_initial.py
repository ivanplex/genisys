# Generated by Django 2.2.4 on 2019-09-03 14:24

from django.db import migrations, models
import django.db.models.deletion


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
                ('quantity', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AtomicRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('atomic_component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='components', to='shop.AtomicComponent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('atomic_requirements', models.ManyToManyField(related_name='requirements', to='shop.AtomicRequirement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlueprintRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('blueprint_component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='components', to='shop.Blueprint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blueprint',
            name='blueprint_requirements',
            field=models.ManyToManyField(related_name='requirements', to='shop.BlueprintRequirement'),
        ),
    ]
