# Generated by Django 4.2.11 on 2024-04-15 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
