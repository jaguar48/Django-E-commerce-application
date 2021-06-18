from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupons(models.Model):
    code = models.CharField(max_length=20,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discounts = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code