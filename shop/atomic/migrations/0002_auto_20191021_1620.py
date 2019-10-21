# Generated by Django 2.2.6 on 2019-10-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0001_initial'),
        ('atomic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atomiccomponent',
            name='attribute',
            field=models.ManyToManyField(related_name='attr', to='attribute.Attribute'),
        ),
        migrations.DeleteModel(
            name='AtomicAttribute',
        ),
    ]
