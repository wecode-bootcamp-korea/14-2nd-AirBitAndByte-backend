# Generated by Django 3.1.2 on 2020-12-04 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201204_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='family_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='given_name',
        ),
    ]