# Generated by Django 2.2.6 on 2019-11-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0038_auto_20191120_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvote_count',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='upvote_count',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]