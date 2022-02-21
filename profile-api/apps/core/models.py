from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Gender(models.TextChoices):
    Male = 'M'
    Female = 'F'

class Profile (models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=1,
        validators=[
            MaxValueValidator(120),
            MinValueValidator(1)
        ])
    sex = models.CharField(max_length=1, choices=Gender.choices, null=True)


    def __str__(self):
        return self.firstName