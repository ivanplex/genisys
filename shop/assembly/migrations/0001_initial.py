# Generated by Django 2.2.5 on 2019-10-08 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atomic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('atomic_prerequisites', models.ManyToManyField(related_name='atomic_requirements', to='atomic.AtomicPrerequisite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('sku', models.CharField(max_length=3)),
                ('availability', models.IntegerField(default=0)),
                ('atomic_specifications', models.ManyToManyField(related_name='atomic_specification', to='atomic.AtomicSpecification')),
                ('blueprint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='based_on', to='assembly.Blueprint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPrerequisite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('min_quantity', models.PositiveIntegerField(default=1)),
                ('max_quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requires', to='assembly.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product_prereq', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='build_with', to='assembly.ProductPrerequisite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute', to='assembly.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_specifications',
            field=models.ManyToManyField(related_name='product_specification', to='assembly.ProductSpecification'),
        ),
        migrations.CreateModel(
            name='BlueprintAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('blueprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blueprint_attribute', to='assembly.Blueprint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blueprint',
            name='product_prerequisites',
            field=models.ManyToManyField(related_name='blueprint_requirements', to='assembly.ProductPrerequisite'),
        ),
    ]
