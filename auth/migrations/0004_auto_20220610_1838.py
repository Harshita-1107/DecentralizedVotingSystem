# Generated by Django 2.1 on 2022-06-10 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20220610_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='adhaar_id',
            new_name='aadhaar_id',
        ),
    ]