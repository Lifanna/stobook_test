# Generated by Django 4.2.6 on 2023-10-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_genre_genreimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeruser',
            old_name='deliveryfirstname',
            new_name='customfirstname',
        ),
        migrations.RenameField(
            model_name='customeruser',
            old_name='deliverysurname',
            new_name='customsurname',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publishing',
        ),
        migrations.RemoveField(
            model_name='deliveryuser',
            name='email',
        ),
        migrations.AlterField(
            model_name='deliveryuser',
            name='deliverysurname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Publishing',
        ),
    ]
