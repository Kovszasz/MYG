# Generated by Django 2.2.6 on 2019-11-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20191031_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='IsPublic',
            field=models.BooleanField(default=True),
        ),
    ]
