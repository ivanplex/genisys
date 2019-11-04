# Generated by Django 2.2.6 on 2019-11-04 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relations', '0001_initial'),
        ('attribute', '0001_initial'),
        ('shop', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtomicComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock_code', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cost', models.FloatField(default=0)),
                ('warehouse_location', models.CharField(blank=True, max_length=255, null=True)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField(default=0)),
                ('availability', models.IntegerField(default=0)),
                ('retail_price', models.FloatField(default=0, verbose_name='Retail Price')),
                ('retail_price_per_unit', models.FloatField(default=0, verbose_name='Retail Price per unit')),
                ('retail_unit_measurement', models.CharField(blank=True, max_length=255, null=True)),
                ('internal_cost', models.FloatField(default=0)),
                ('attribute', models.ManyToManyField(related_name='atom_attr', to='attribute.Attribute')),
                ('image_urls', models.ManyToManyField(related_name='atomic_image_urls', to='shop.URL')),
                ('offset_image_urls', models.ManyToManyField(related_name='offset_atomic_image_urls', to='shop.OffsetImageURL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AtomicGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='group.Group')),
                ('members', models.ManyToManyField(related_name='members', to='atomic.AtomicComponent')),
            ],
            options={
                'abstract': False,
            },
            bases=('group.group',),
        ),
        migrations.CreateModel(
            name='AtomicPrerequisite',
            fields=[
                ('prerequisite_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relations.Prerequisite')),
                ('virtual', models.BooleanField(default=False)),
                ('atomic_component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='requires', to='atomic.AtomicComponent')),
                ('atomic_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='allowed_group', to='atomic.AtomicGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=('relations.prerequisite',),
        ),
        migrations.CreateModel(
            name='AtomicSpecification',
            fields=[
                ('specification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relations.Specification')),
                ('prerequisite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='build_with', to='atomic.AtomicPrerequisite')),
                ('selected_component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='using', to='atomic.AtomicComponent')),
            ],
            options={
                'abstract': False,
            },
            bases=('relations.specification',),
        ),
    ]
