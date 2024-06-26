# Generated by Django 4.2.11 on 2024-04-08 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_auto_20240408_1528"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
