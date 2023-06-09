# Generated by Django 4.1.2 on 2023-02-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0003_alter_competition_teams"),
    ]

    operations = [
        migrations.AlterField(
            model_name="competition",
            name="teams",
            field=models.ManyToManyField(
                blank=True, related_name="competition", to="players.team"
            ),
        ),
    ]
