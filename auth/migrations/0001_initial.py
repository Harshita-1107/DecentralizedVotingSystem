# Generated by Django 2.1 on 2022-06-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveVoters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.CharField(max_length=500)),
                ('has_voted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhaar_id', models.CharField(max_length=16)),
                ('thumb_id', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=500)),
                ('birth_date', models.DateField(null=True)),
                ('locality', models.CharField(max_length=500)),
            ],
        ),
    ]
