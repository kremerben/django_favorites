from django.db import models

# Create your models here.

class War(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()

    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Battle(models.Model):
    name = models.CharField(max_length=100)
    date = models.IntegerField()
    location = models.CharField(max_length=120)
    war = models.ForeignKey(War, related_name='war')
    winner = models.ForeignKey(Country, related_name='winner')
    loser = models.ForeignKey(Country, related_name='loser')

    def __unicode__(self):
        return self.name


class Military(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='country')
    allies = models.ForeignKey(Country, related_name='allies')
    enemy = models.ForeignKey(Country, related_name='enemy')

    def __unicode__(self):
        return self.name


class Commander(models.Model):
    name = models.CharField(max_length=100)
    military = models.ForeignKey(Military, related_name='military')
    battle = models.ForeignKey(Battle, related_name='battle')

    def __unicode__(self):
        return self.name
