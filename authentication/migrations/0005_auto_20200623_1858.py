# Generated by Django 3.0.6 on 2020-06-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20200623_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp_exp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
