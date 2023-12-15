from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False)
    player_id = models.IntegerField(primary_key=True, null=False)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.username + " " + str(self.player_id)



class Field(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    duration = models.IntegerField(null=False)
    field_id = models.IntegerField(primary_key=True, null=False)

    def __str__(self):
        return self.name + " " + self.address + " " + str(self.duration) + " " + str(self.field_id)



class Sport(models.Model):
    name = models.CharField(max_length=50, null=False)
    sport_id = models.IntegerField(primary_key=True, null=False)

    def __str__(self):
        return self.name + " " + str(self.sport_id)