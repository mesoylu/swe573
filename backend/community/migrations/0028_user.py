# Generated by Django 2.2.6 on 2019-11-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0027_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.SlugField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='images')),
                ('date_registered', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]