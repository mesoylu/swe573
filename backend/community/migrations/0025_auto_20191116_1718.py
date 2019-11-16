# Generated by Django 2.2.6 on 2019-11-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0024_datafield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafield',
            name='type',
            field=models.CharField(choices=[('str', 'string'), ('bl', 'boolean'), ('dec', 'decimal'), ('fl', 'float'), ('dur', 'duration'), ('dt', 'dateTime'), ('uri', 'anyURI')], max_length=3),
        ),
    ]