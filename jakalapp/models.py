from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    flag = models.ImageField(upload_to="icons/country/")
    continent = models.CharField(max_length=200)

class Sponsor(models.Model):
    name = models.CharField(max_length = 200)
    logo = models.ImageField(upload_to="icons/logo/")

class Franchise(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="icons/franchise/")

class Character(models.Model):
    name = models.CharField(max_length = 200)
    icon = models.ImageField(upload_to="icons/character/")
    franchise = models.ForeignKey(Franchise, on_delete=models.DO_NOTHING)

class Player(models.Model):
    name = models.CharField(max_length = 200, verbose_name="Name")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Country")
    rank = models.IntegerField(verbose_name="Rank")
    main = models.ForeignKey(Character, on_delete=models.DO_NOTHING, verbose_name="Main")
    team = models.ForeignKey(Sponsor, on_delete=models.DO_NOTHING, verbose_name="Sponsor")