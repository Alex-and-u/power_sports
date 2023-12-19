from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.username


class Field(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return self.name + " " + self.address + " " + str(
            self.duration)


class Sport(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
