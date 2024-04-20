# Generated by Django 5.0.1 on 2024-01-29 06:54

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0007_alter_book_issue_due_date_alter_reader_guardian_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='book_instance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lims_app.bookinstance'),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 23, 54, 22, 285268), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='reader_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lims_app.reader'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='guardian_name',
            field=models.CharField(help_text='parent/guardian name', max_length=100),
        ),
    ]
