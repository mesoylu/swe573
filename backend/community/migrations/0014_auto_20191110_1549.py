# Generated by Django 2.2.6 on 2019-11-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_datatype_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafield',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.DataFieldType'),
        ),
    ]
