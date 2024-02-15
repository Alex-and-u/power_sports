from django.contrib import admin
from .models import Field, City, Address, Booking

# Register your models here.
admin.site.register(Field)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Booking)
