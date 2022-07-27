from django.db import models
from django.forms import CharField, ImageField

# Create your models here.


class Bot_token(models.Model):
    token = models.TextField()

    def __str__(self):
        return self.token


class Chat_id(models.Model):
    chat_id = models.TextField()

    def __str__(self):
        return self.chat_id


class Site_logo(models.Model):
    shortcut_ico = models.ImageField()
    image = models.ImageField(upload_to='site_logo')


class Banner(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='banner_image')
    background_image = models.ImageField(upload_to='banner_background_image')

    def __str__(self):
        return self.title



class Feauters(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    feature1 = models.CharField(max_length=50)
    feature2 = models.CharField(max_length=50)
    feature3 = models.CharField(max_length=50)
    feature4 = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Testimionals(models.Model):
    image = models.ImageField(upload_to='testimionals_images')



class About(models.Model):
    image1 = models.ImageField(upload_to='about_images')
    image2 = models.ImageField(upload_to='about_images')
    image3 = models.ImageField(upload_to='about_images')
    image4 = models.ImageField(upload_to='about_images')
    title = models.CharField(max_length=255)
    text = models.TextField()
    topic_title1 = models.CharField(max_length=150)
    topic_text1 = models.TextField()
    topic_title2 = models.CharField(max_length=150)
    topic_text2 = models.TextField()




class Intro_video(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    background_image = models.ImageField(upload_to='video_background_image')
    video_url = models.CharField(max_length=555)

    def __str__(self):
        return self.title



class Services_text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Services(models.Model):
    image = models.ImageField(upload_to='services_images')
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title



class Testimionals_text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    # inson rasmlari
    image1 = models.ImageField(upload_to='testimionals_text_images')
    image2 = models.ImageField(upload_to='testimionals_text_images')
    image3 = models.ImageField(upload_to='testimionals_text_images')
    image4 = models.ImageField(upload_to='testimionals_text_images')
    image5 = models.ImageField(upload_to='testimionals_text_images')
    image6 = models.ImageField(upload_to='testimionals_text_images')


    def __str__(self):
        return self.title



class Feedbacks(models.Model):
    feedback = models.TextField()
    image = models.ImageField()
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)


    def __str__(self):
        return self.name




class Packages_text(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title


class Left_package(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField() 
    timeframe = models.CharField(max_length=55)
    offer1 = models.CharField(max_length=155)
    offer2 = models.CharField(max_length=155)
    offer3 = models.CharField(max_length=155)
    offer4 = models.CharField(max_length=155)
    offer5 = models.CharField(max_length=155)


class Center_package(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField() 
    timeframe = models.CharField(max_length=55)
    offer1 = models.CharField(max_length=155)
    offer2 = models.CharField(max_length=155)
    offer3 = models.CharField(max_length=155)
    offer4 = models.CharField(max_length=155)
    offer5 = models.CharField(max_length=155)



class Right_package(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField() 
    timeframe = models.CharField(max_length=55)
    offer1 = models.CharField(max_length=155)
    offer2 = models.CharField(max_length=155)
    offer3 = models.CharField(max_length=155)
    offer4 = models.CharField(max_length=155)
    offer5 = models.CharField(max_length=155)


 

class Number_form_text(models.Model):
    background_image = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.title


class Footer_text(models.Model):
    text = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

