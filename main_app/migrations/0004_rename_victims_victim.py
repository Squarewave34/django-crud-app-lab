# Generated by Django 5.1.5 on 2025-02-02 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_victims'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Victims',
            new_name='Victim',
        ),
    ]
