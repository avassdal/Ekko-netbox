# Generated by Django 4.0.5 on 2022-06-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0155_interface_poe_mode_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
