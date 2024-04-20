# Generated by Django 5.0.1 on 2024-01-29 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0008_alter_book_issue_book_instance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='lims_app.reader'),
        ),
        migrations.DeleteModel(
            name='Book_Issue',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]