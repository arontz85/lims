# Generated by Django 5.0.1 on 2024-01-28 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0006_remove_reader_reading_reader_guardian_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 11, 42, 39, 132329), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='guardian_name',
            field=models.CharField(help_text='parent/guardian full name', max_length=100),
        ),
        migrations.AlterField(
            model_name='reader',
            name='reader_email',
            field=models.EmailField(help_text='Guardian/parent e-mail', max_length=100),
        ),
    ]
