# Generated by Django 5.0.4 on 2024-05-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_booking"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=100)),
                ("shift", models.IntegerField()),
            ],
        ),
    ]
