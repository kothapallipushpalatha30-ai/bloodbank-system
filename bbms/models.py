from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group_needed = models.CharField(max_length=5)
    hospital_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name