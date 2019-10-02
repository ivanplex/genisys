# Generated by Django 2.2.5 on 2019-10-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0002_blueprintattribute'),
        ('group', '0003_productgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlueprintGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(related_name='members', to='assembly.Blueprint')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
