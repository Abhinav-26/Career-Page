from django.db import models
from django.db.models.base import ModelState

# Create your models here.
class Jobs(models.Model):
    position = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    jobType = models.CharField(max_length=500)
    openings = models.IntegerField()
    experiences = models.CharField(max_length=500)
    educationLevel = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=6000)
    requirements = models.TextField(max_length=6000)

    def __str__(self) :
        return self.position


class Application(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    mob = models.CharField(max_length=10)
    mailID = models.CharField(max_length=50)
    resume = models.FileField(upload_to="resume/")
