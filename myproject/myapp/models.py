from django.db import models

# Create your models here.

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


class Drinks(models.Model):

    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory,on_delete=models.PROTECT,default=None)

class Booking(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    commentarios = models.CharField(max_length=1000)


class Employees(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name
    

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name