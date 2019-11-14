# Generated by Django 2.2.6 on 2019-11-14 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0001_initial'),
    ]

    operations = [
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
    ]