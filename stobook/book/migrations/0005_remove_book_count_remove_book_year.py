# Generated by Django 4.2.6 on 2023-10-27 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_publishing_rename_firstname_author_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),
    ]