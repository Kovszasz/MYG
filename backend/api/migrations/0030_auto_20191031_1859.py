# Generated by Django 2.2.6 on 2019-10-31 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20191027_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='IMG',
            field=models.ImageField(blank=True, default='', upload_to='post'),
        ),
    ]