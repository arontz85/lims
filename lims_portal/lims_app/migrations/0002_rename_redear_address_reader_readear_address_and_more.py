# Generated by Django 5.0.1 on 2024-01-24 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='redear_address',
            new_name='readear_address',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='redear_contact',
            new_name='readear_contact',
        ),
    ]
