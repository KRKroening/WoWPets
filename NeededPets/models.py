from django.db import models

# Create your models here.

class PetsToCollect(models.Model):
    creatureId = models.IntegerField()
    creatureName = models.TextField()
    source = models.CharField(max_length=300)
    zone = models.TextField()
    # Vendor, Ach, Drop, Profession, ect
    investmentType = models.CharField(max_length=1)
    # Drop rate, gold value, Achiev ID
    investmentValue = models.IntegerField()