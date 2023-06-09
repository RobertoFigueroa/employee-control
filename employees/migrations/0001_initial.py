# Generated by Django 4.1.7 on 2023-03-31 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(editable=False, max_length=12)),
                ("names", models.CharField(max_length=100)),
                ("last_names", models.CharField(max_length=100)),
                ("date", models.DateField(blank=True, null=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="departments.department",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Employees",
            },
        ),
    ]
