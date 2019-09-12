# Generated by Django 2.2.5 on 2019-09-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blueprint',
            old_name='build_prerequisites',
            new_name='product_prerequisites',
        ),
        migrations.RenameField(
            model_name='productprerequisite',
            old_name='build',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='productspecification',
            old_name='build_prereq',
            new_name='product_prereq',
        ),
        migrations.RemoveField(
            model_name='product',
            name='build_specifications',
        ),
        migrations.AddField(
            model_name='product',
            name='product_specifications',
            field=models.ManyToManyField(related_name='product_specification', to='assembly.ProductSpecification'),
        ),
    ]
