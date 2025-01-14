# Create your models here.

from django.db import models

TABLES_COLORS = (
    ('BLACK', 'BLACK'),
    ('WHITE', 'WHITE'),
    ('RED', 'RED'),
    ('GREEN', 'GREEN'),
)

TABLES_LEGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)

class Table(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10, choices=TABLES_COLORS)
    legs = models.CharField(max_length=2, choices=TABLES_LEGS)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    available = models.BooleanField()

