# Generated by Django 5.0.3 on 2024-05-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0009_rename_telephone_voyager_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voyager',
            old_name='phone',
            new_name='telephone',
        ),
    ]
