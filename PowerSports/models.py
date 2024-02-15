from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.username


class Field(models.Model):
    name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    date_time = models.DateTimeField()
    duration = models.IntegerField(null=False)

    def __str__(self):
        return self.name + " " + self.address + " " + str(
            self.duration)


class Sport(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=150, default='')
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Booking(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    no_of_players = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now=True)
    time = models.CharField(max_length=50, default='')





