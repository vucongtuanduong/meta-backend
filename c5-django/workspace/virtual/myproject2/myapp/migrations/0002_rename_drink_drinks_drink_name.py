# Generated by Django 4.2.6 on 2023-10-28 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinks',
            old_name='drink',
            new_name='drink_name',
        ),
    ]
