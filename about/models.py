from turtle import position
from django.db import models

# Create your models here.







class About_us(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    title1 = models.CharField(max_length=255)
    text1 = models.TextField()

    title2 = models.CharField(max_length=255)
    text2 = models.TextField()

    image1 = models.ImageField(upload_to='about_images')
    image2 = models.ImageField(upload_to='about_images')
    image3 = models.ImageField(upload_to='about_images')
    image4 = models.ImageField(upload_to='about_images')

    def __str__(self):
        return self.title



class Team_text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.title



class Team(models.Model):
    image = models.ImageField(upload_to='team_images')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.name