# Generated by Django 5.0.3 on 2024-05-18 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0008_voyager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voyager',
            old_name='telephone',
            new_name='phone',
        ),
    ]
