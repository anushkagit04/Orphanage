from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=121)
    email = models.CharField(max_length=121)
    phone = models.CharField(max_length=12)
    age = models.CharField(max_length=10)
    feedback = models.CharField(max_length=121)
    date = models.DateField()
    
    def __str__(self):
        return self.name

class Donate(models.Model):
    name = models.CharField(max_length=121)
    email = models.CharField(max_length=121)  
    password = models.CharField(max_length=121)
    phone = models.CharField(max_length=121)
    address = models.CharField(max_length=121)
    donation = models.CharField(max_length=121)
    date = models.DateField()

    def __str__(self):
        return self.name
