# Generated by Django 2.2.6 on 2019-11-18 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguratorStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('selected', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]
