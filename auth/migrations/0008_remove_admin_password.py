# Generated by Django 2.1 on 2022-06-17 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20220617_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='password',
        ),
    ]