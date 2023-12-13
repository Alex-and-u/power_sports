from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False)
    player_id = models.DecimalField(max_length=10, primary_key=True, null=True)



class Field(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    field_id = models.DecimalField(max_length=10, primary_key=True, null=True)





class Sport(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    sport_id = models.DecimalField(max_length=10, primary_key=True, null=True)