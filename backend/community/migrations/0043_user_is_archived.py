# Generated by Django 2.2.6 on 2019-11-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0042_auto_20191123_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
