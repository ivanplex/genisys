# Generated by Django 2.2.4 on 2019-09-05 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtomicRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('min_quantity', models.PositiveIntegerField(default=1)),
                ('max_quantity', models.PositiveIntegerField(default=1)),
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
                ('atomic_requirements', models.ManyToManyField(related_name='requirements', to='concept.AtomicRequirement')),
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
                ('min_quantity', models.PositiveIntegerField(default=1)),
                ('max_quantity', models.PositiveIntegerField(default=1)),
                ('blueprint_component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='components', to='concept.Blueprint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blueprint',
            name='blueprint_requirements',
            field=models.ManyToManyField(related_name='requirements', to='concept.BlueprintRequirement'),
        ),
    ]
