# Generated by Django 4.2.6 on 2023-10-29 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_remove_book_count_remove_book_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='surname',
        ),
    ]
