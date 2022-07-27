from django.db import models

# Create your models here.




class Services_text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title



class Services(models.Model): 
    image = models.ImageField(upload_to='services_images')
    title = models.CharField(max_length=155)
    text = models.TextField()


    def __str__(self):
        return self.title


class Explaining(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    service1 = models.CharField(max_length=55)
    service2 = models.CharField(max_length=55)
    service3 = models.CharField(max_length=55)
    service4 = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Services_introduction(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    cause1 = models.CharField(max_length=255)
    cause2 = models.CharField(max_length=255)
    cause3 = models.CharField(max_length=255)
    cause4 = models.CharField(max_length=255)
    cause5 = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services_images')

    def __str__(self):
        return self.title



