# Generated by Django 2.2.6 on 2019-10-25 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20191025_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalscoringprofile',
            name='label',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Label'),
        ),
    ]
