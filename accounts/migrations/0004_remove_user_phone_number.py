# Generated by Django 3.0.3 on 2020-03-18 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
