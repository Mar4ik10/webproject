# Generated by Django 4.2.1 on 2023-05-27 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutModel',
            new_name='ContactModel',
        ),
        migrations.RenameModel(
            old_name='AboutUrlsModel',
            new_name='ContactUrlsModel',
        ),
    ]
