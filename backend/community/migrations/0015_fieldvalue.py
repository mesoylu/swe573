# Generated by Django 2.2.6 on 2019-11-10 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_auto_20191110_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('data_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.DataField')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.Post')),
            ],
        ),
    ]
