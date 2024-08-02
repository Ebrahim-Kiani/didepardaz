from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    country = CountryField()

    def __str__(self):
        return self.name


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False, unique=True)
    price = models.PositiveIntegerField(blank=False, null=False)
    color = models.CharField(max_length=20, blank=False, null=False)
    screen_size = models.PositiveIntegerField(blank=False, null=False)
    available = models.BooleanField(blank=False, null=False)
    country = CountryField()

    def __str__(self):
        return f"brand name : {self.brand.name}, model : {self.model}"
