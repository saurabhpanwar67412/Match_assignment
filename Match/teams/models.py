from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    clubState = models.CharField(max_length=100)
    logoUri = models.ImageField(upload_to='media/teams/img/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, default='')
    imageUri = models.ImageField(upload_to='media/players/img/')
    jerseyNumber = models.PositiveIntegerField()
    Country = models.CharField(max_length=70)

    def __str__(self):
        return self.firstName

class Matches(models.Model):
    matchesBetweenteams = models.CharField(max_length=100)
    Winner = models.CharField(max_length= 100)
    def __str__(self):
        return self.matchesBetweenteams


class Points(models.Model):
    points = models.IntegerField(default=0)
    teampoints = models.CharField(max_length= 100)

    def __str__(self):
        return self.teampoints








