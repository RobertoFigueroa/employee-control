# Generated by Django 4.1.7 on 2023-03-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="code",
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
