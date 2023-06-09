# Generated by Django 4.1.2 on 2023-02-27 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.TextField()),
                (
                    "country",
                    models.TextField(
                        choices=[
                            ("ENG", "England"),
                            ("RU", "Russia"),
                            ("ESP", "Spain"),
                            ("BRA", "Brazil"),
                        ]
                    ),
                ),
                ("city", models.TextField(blank=True, default="")),
            ],
        ),
        migrations.CreateModel(
            name="Player",
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
                ("name", models.TextField()),
                (
                    "country",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("ENG", "England"),
                            ("RU", "Russia"),
                            ("ESP", "Spain"),
                            ("BRA", "Brazil"),
                        ],
                        default="",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="players.team",
                    ),
                ),
            ],
        ),
    ]
