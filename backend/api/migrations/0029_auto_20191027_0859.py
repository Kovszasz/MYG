# Generated by Django 2.2.6 on 2019-10-27 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0028_auto_20191026_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='type',
            field=models.CharField(choices=[('None', 'None'), ('Like', 'Like'), ('View', 'View'), ('Click', 'Click'), ('Favourite', 'Favourite')], max_length=100),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='channel', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
