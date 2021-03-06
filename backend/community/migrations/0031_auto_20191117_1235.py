# Generated by Django 2.2.6 on 2019-11-17 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0030_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafield',
            name='community',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.Community'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datafield',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datatype',
            name='community',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.Community'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datatype',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='community',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.Community'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='community.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.User'),
        ),
    ]
