# Generated by Django 5.0.3 on 2024-05-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0013_alter_purchase_date_alter_purchase_voyage'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='active_travelers',
            field=models.IntegerField(null=True),
        ),
    ]
