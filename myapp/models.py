from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    contact = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)
    clinic_address = models.TextField()

    def __str__(self):
        return self.name
    

    