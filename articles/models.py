from django.db import models

# Create your models here.


class Article(models.Model):
    unit_kg = 'Kg'
    unit_gr = 'gr'
    unit_t = 'T'

    UNIT_CHOICES = [
        (unit_kg, 'Kg'),
        (unit_gr, 'gr'),
        (unit_t, 'T'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    serial = models.CharField(max_length=200)
    unit = models.CharField(
        max_length=10, choices=UNIT_CHOICES, default=unit_kg)
    weight = models.PositiveIntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
