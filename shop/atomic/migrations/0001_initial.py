# Generated by Django 2.2.6 on 2019-10-09 10:02

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
                ('type', models.CharField(blank=True, max_length=255, null=True)),
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
        migrations.CreateModel(
            name='AtomicPrerequisite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('min_quantity', models.PositiveIntegerField(default=1)),
                ('max_quantity', models.PositiveIntegerField(default=1)),
                ('atomic_component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requires', to='atomic.AtomicComponent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AtomicSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('atomic_prereq', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='build_with', to='atomic.AtomicPrerequisite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AtomicAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('atomic_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atom_attribute', to='atomic.AtomicComponent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
