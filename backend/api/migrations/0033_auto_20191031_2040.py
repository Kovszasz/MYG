# Generated by Django 2.2.6 on 2019-10-31 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20191031_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='mimeuser',
            name='IsOfficial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mimeuser',
            name='sex',
            field=models.BooleanField(default=True),
        ),
    ]
