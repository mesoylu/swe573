# Generated by Django 2.2.6 on 2019-11-16 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_fieldvalue_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldvalue',
            name='community',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_values',
        ),
        migrations.AddField(
            model_name='fieldvalue',
            name='Post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.Post'),
            preserve_default=False,
        ),
    ]
