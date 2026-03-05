from django.db import models

# Create your models here.
class Employees(models.Model):
    First_name=models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    Role=models.CharField(max_length=200)
    Shift=models.IntegerField()

    def __str__(self):
        return self.First_name


