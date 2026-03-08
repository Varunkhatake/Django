from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.TextField(blank=True)

    