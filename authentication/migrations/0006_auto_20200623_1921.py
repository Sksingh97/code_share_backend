# Generated by Django 3.0.6 on 2020-06-23 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20200623_1858'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
