from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False)
    player_id = models.IntegerField(primary_key=True, null=False)



class Field(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    field_id = models.IntegerField(primary_key=True, null=False)



class Sport(models.Model):
    name = models.CharField(max_length=50, null=False)
    sport_id = models.IntegerField(primary_key=True, null=False)