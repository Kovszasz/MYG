# Generated by Django 2.2.6 on 2019-10-16 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('api', '0009_mods'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertSettings',
            fields=[
                ('admin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('AdFrequency', models.IntegerField(default=50)),
                ('MoneyForSeen', models.FloatField(default=0)),
                ('MoneyForClick', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('date', models.DateField(auto_now_add=True)),
                ('content_post', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Post')),
                ('post_from_last_advert', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MimeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile')),
                ('IsAdvertiser', models.BooleanField(default=False)),
                ('company', models.CharField(default='', max_length=100)),
                ('balance', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
