# Generated by Django 3.0.3 on 2020-03-20 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
