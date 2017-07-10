from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    age = models.CharField(max_length=3)
    problem = models.CharField(max_length=1000)
    report = models.FileField()

    def __str__(self):
        return self.name

