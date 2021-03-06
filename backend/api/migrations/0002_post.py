# Generated by Django 2.2.6 on 2019-10-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('IMG', models.ImageField(blank=True, upload_to='post')),
                ('IsModerated', models.BooleanField(default=False)),
                ('IsAdvert', models.BooleanField(default=False)),
                ('IsInlinePost', models.BooleanField(default=False)),
                ('URL', models.URLField(default='', max_length=250)),
                ('AppearenceFrequency', models.IntegerField(default=1)),
                ('NumberOfLikes', models.IntegerField(default=0)),
            ],
        ),
    ]
