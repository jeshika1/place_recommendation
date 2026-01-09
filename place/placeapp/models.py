from django.db import models

# Create your models here.
from django.db import models

class UserPreference(models.Model):
    budget = models.IntegerField()
    food_type = models.CharField(max_length=20)
    people = models.IntegerField()
    location = models.CharField(max_length=100)
    vibe = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=100)
    extra = models.TextField(blank=True)

    def __str__(self):
        return f"{self.location} - {self.food_type} - {self.people} people"
