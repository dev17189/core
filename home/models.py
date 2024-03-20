from django.db import models

# Create your models here.

class Voters(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=100)
    address = models.TextField()

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=25)
    constituency = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class Car(models.Model):
    car_model = models.CharField(max_length=100)
    max_speed = models.IntegerField(default=25)
    
    def __str__(self) -> str:
        return self.car_model