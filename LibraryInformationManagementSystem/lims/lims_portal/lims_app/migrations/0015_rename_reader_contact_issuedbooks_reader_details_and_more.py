# Generated by Django 5.0.1 on 2024-02-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0014_issuedbooks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbooks',
            old_name='reader_contact',
            new_name='reader_details',
        ),
        migrations.RemoveField(
            model_name='issuedbooks',
            name='overdue_fee',
        ),
        migrations.RemoveField(
            model_name='issuedbooks',
            name='reader_email',
        ),
        migrations.RemoveField(
            model_name='issuedbooks',
            name='reader_name',
        ),
        migrations.RemoveField(
            model_name='issuedbooks',
            name='reference_id',
        ),
        migrations.AddField(
            model_name='issuedbooks',
            name='book_condition',
            field=models.CharField(default='In good condition', max_length=200),
        ),
    ]
