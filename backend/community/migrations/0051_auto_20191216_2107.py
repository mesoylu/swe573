# Generated by Django 2.2.6 on 2019-12-16 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0050_auto_20191215_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='community.DataType'),
        ),
    ]
