# Generated by Django 3.0.9 on 2020-08-26 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_form',
            new_name='user_from',
        ),
    ]
