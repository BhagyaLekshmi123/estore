# Generated by Django 4.1.1 on 2022-10-06 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_name_books_book_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='book_name',
            new_name='name',
        ),
    ]
