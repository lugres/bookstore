# Generated by Django 4.2.11 on 2024-04-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
