# Generated by Django 5.0.1 on 2024-01-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0011_alter_book_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(blank=True, null=True, to='lims_app.reader'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=200),
        ),
    ]