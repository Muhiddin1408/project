from django.db import models

# Create your models here.





class Contact_info(models.Model):
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=155)
    number2 = models.CharField(max_length=155, blank=True)
    email = models.CharField(max_length=155, blank=True)

    def __str__(self):
        return self.address



class Address(models.Model):
    address = models.CharField(max_length=455)

    def __str__(self):
        return self.address
