from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    country = CountryField(db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False, unique=True)
    price = models.PositiveIntegerField(blank=False, null=False)
    color = models.CharField(max_length=20, blank=False, null=False)
    screen_size = models.DecimalField(
        max_digits=9,  # Adjust the max_digits and decimal_places as needed
        decimal_places=1,  # For example, allows values like 123.45
        blank=False,
        null=False,
        validators=[MinValueValidator(0.0)]
    )
    is_available = models.BooleanField(blank=False, null=False)
    country = CountryField(db_index=True)

    def __str__(self):
        return f"brand name : {self.brand.name}, model : {self.model}"
