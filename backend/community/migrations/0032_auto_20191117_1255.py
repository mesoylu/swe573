# Generated by Django 2.2.6 on 2019-11-17 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0031_auto_20191117_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datatype',
            old_name='data_fields',
            new_name='fields',
        ),
    ]
