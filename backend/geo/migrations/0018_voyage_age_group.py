# Generated by Django 5.0.3 on 2024-06-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0017_alter_voyage_active_travelers'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='age_group',
            field=models.CharField(choices=[('18-30', '18-30'), ('30-45', '30-45'), ('45+', '45+')], default='18-30', max_length=10),
        ),
    ]
