# Generated by Django 2.2.6 on 2020-01-22 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('atomic', '0001_initial'),
        ('relations', '0001_initial'),
        ('modular_assembly', '0001_initial'),
        ('attribute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('human_readable_name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('retail_price', models.FloatField(default=0, verbose_name='Retail Price')),
                ('retail_price_per_unit', models.FloatField(default=0, verbose_name='Retail Price per unit')),
                ('retail_unit_measurement', models.CharField(blank=True, max_length=255, null=True)),
                ('internal_cost', models.FloatField(default=0)),
                ('component_factor', models.FloatField(default=None, null=True)),
                ('build_time', models.PositiveIntegerField(default=0)),
                ('atomic_prerequisites', models.ManyToManyField(related_name='atomic_requirements', to='atomic.AtomicPrerequisite')),
                ('description_images', models.ManyToManyField(related_name='blueprint_description_image', to='modular_assembly.URL')),
                ('illustration_images', models.ManyToManyField(related_name='blueprint_illustration', to='modular_assembly.OffsetImageURL')),
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
                ('sku', models.CharField(max_length=255, unique=True)),
                ('human_readable_name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('availability', models.IntegerField(default=0)),
                ('retail_price', models.FloatField(default=0, verbose_name='Retail Price')),
                ('retail_price_per_unit', models.FloatField(default=0, verbose_name='Retail Price per unit')),
                ('retail_unit_measurement', models.CharField(blank=True, max_length=255, null=True)),
                ('internal_cost', models.FloatField(default=0)),
                ('component_factor', models.FloatField(default=None, null=True)),
                ('atomic_specifications', models.ManyToManyField(related_name='atomic_specification', to='atomic.AtomicSpecification')),
                ('attribute', models.ManyToManyField(related_name='product_attr', to='attribute.Attribute')),
                ('blueprint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='based_on', to='assembly.Blueprint')),
                ('description_images', models.ManyToManyField(related_name='description_image', to='modular_assembly.URL')),
                ('illustration_images', models.ManyToManyField(related_name='illustration_image', to='modular_assembly.OffsetImageURL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='group.Group')),
                ('members', models.ManyToManyField(related_name='members', to='assembly.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=('group.group',),
        ),
        migrations.CreateModel(
            name='ProductPrerequisite',
            fields=[
                ('prerequisite_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relations.Prerequisite')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='requires', to='assembly.Product')),
                ('product_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='allowed_group', to='assembly.ProductGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=('relations.prerequisite',),
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('specification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relations.Specification')),
                ('prerequisite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='build_with', to='assembly.ProductPrerequisite')),
                ('selected_component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='using', to='assembly.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=('relations.specification',),
        ),
        migrations.AddField(
            model_name='product',
            name='product_specifications',
            field=models.ManyToManyField(related_name='product_specification', to='assembly.ProductSpecification'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='thumbnail_image', to='modular_assembly.URL'),
        ),
        migrations.CreateModel(
            name='BlueprintGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='group.Group')),
                ('members', models.ManyToManyField(related_name='members', to='assembly.Blueprint')),
            ],
            options={
                'abstract': False,
            },
            bases=('group.group',),
        ),
        migrations.CreateModel(
            name='BlueprintAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('blueprint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blueprint_attribute', to='assembly.Blueprint')),
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
        migrations.AddField(
            model_name='blueprint',
            name='thumbnail_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blueprint_thumbnail', to='modular_assembly.URL'),
        ),
    ]
