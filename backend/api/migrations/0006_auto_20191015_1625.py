# Generated by Django 2.2.6 on 2019-10-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_to',
        ),
        migrations.AddField(
            model_name='comment',
            name='ID',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False),
        ),
    ]
