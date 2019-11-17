# Generated by Django 2.2.6 on 2019-11-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0035_community_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datatype',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='datatype',
            name='body',
        ),
        migrations.AddField(
            model_name='datatype',
            name='description',
            field=models.CharField(default='adsdasd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.SlugField(default=112213, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='communities', to='community.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='community.User'),
        ),
    ]
