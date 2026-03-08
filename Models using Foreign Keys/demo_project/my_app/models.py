from django.db import models

# Create your models here.
class drinkCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class drink(models.Model):
    name = models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.ForeignKey(drinkCategory,on_delete=models.PROTECT,default=None)

    def __str__(self):
        return self.name