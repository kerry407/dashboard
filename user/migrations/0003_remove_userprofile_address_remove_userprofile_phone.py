# Generated by Django 4.0.4 on 2022-05-03 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userprofile_city_remove_userprofile_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]
