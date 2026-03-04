from django.db import models
# Create your models here.
class Booking(models.Model):
    First_name=models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    gest_count=models.IntegerField()
    reservation_time=models.DateTimeField(auto_now=True)
    comments=models.CharField(max_length=200)
    def __str__(self):
        return self.name