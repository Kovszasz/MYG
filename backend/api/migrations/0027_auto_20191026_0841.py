# Generated by Django 2.2.6 on 2019-10-26 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20191026_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memecontent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='memecontent',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='score', to='api.Post'),
        ),
    ]
