from __future__ import unicode_literals

from django.db import models

class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

class Scholarship(models.Model):
    name = models.CharField(max_length=50)


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)



# Create your models here.
