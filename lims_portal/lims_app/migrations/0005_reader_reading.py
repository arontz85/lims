# Generated by Django 5.0.1 on 2024-01-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='reading',
            field=models.ManyToManyField(blank=True, to='lims_app.book'),
        ),
    ]