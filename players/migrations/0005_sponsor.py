# Generated by Django 4.1.2 on 2023-02-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0004_alter_competition_teams"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sponsor",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
    ]
