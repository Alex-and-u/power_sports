from django.contrib.auth.models import User
from django.contrib.gis.geoip2.resources import City
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


# class Town(models.Model):
#     name_town = models.CharField(max_lenght=50, null=False)
#     name_county = models.CharField(max_length=50, null=False)

class Location(models.Model):
    name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    # new_city = models.ForeignKey(City, related_name='venuecity', null=True, on_delete=models.CASCADE)

    latitude = models.DecimalField(max_digits=17, decimal_places=14, default=0)
    longitude = models.DecimalField(max_digits=17, decimal_places=14, default=0)

    def __unicode__(self):
        return self.name
#
# class Location(models.Model):
#     continent = models.ForeignKey(Continent)
#     country = ChainedForeignKey(
#         Country,
#         chained_field="continent",  # Location.continent
#         chained_model_field="continent",  # Country.continent
#         show_all=False,  # only the filtered results should be shown
#         auto_choose=True,
#         sort=True)