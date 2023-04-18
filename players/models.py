from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


def get_year():
    return timezone.now().year


class Country(TextChoices):
    ENGLAND = 'ENG', 'England'
    RUS = 'RU', 'Russia'
    ESP = 'ESP', 'Spain'
    BRA = 'BRA', 'Brazil'


class Team(models.Model):
    name = models.TextField()
    country = models.TextField(choices=Country.choices)
    city = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.id} {self.name}: {self.get_country_display()}'


class Player(models.Model):
    name = models.TextField()
    country = models.TextField(choices=Country.choices, default='', blank=True)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} - {self.get_country_display()}'


class Competition(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=30, default=get_year)
    teams = models.ManyToManyField(Team, blank=True, related_name='competition')

    def __str__(self):
        return f'{self.name} - {self.year}'


class Sponsor(models.Model):
    name = models.CharField(max_length=30)
    team = models.ManyToManyField(
        Team,
        related_name='sponsor',
        through='sponsorship',
    )

    def __str__(self):
        return f'{self.name}'


class Sponsorship(models.Model):
    sponsor = models.ForeignKey(Sponsor,
                                on_delete=models.CASCADE)
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,
                                 max_digits=16)






