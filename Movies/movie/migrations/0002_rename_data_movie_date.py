# Generated by Django 4.0.4 on 2022-05-29 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='data',
            new_name='date',
        ),
    ]
