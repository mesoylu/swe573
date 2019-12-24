# Generated by Django 2.2.6 on 2019-11-20 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0036_auto_20191117_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafield',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data_fields', to='community.Community'),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data_types', to='community.Community'),
        ),
        migrations.AlterField(
            model_name='post',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='community_posts', to='community.Community'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_posts', to='community.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
