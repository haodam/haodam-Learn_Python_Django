from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

class Python2104(models.Model):
    ten = models.CharField(max_length= 50)
    tuoi = models.IntegerField()
    diachi = models.TextField()

    class Meta:
        db_table = "Python2104"

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

    class Meta:
        db_table = "Place"

class Restaurant(models.Model):

    place = models.OneToOneField(
        "Place",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

    class Meta:
        db_table ="Restaurant"

class Reporter(models.Model):
    first_name = models.CharField("Ten" , max_length=30)
    last_name = models.CharField("Ho", max_length=30)
    email = models.EmailField("Email")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    class Meta:
        db_table ="Reporter"

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
        db_table = "Article"

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
        db_table ="Publication"

    def __str__(self):
        return self.title


class BaiBao(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']
        db_table = "BaiBao"

    def __str__(self):
        return self.headline
    
class UserAvarta(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key= True
    )
    avarta = models.ImageField(upload_to ="avarta")
    
    class Meta:
        db_table = "UserAvarta"



    
#Command
# python manage.py makemigrations <Ten app> kiem tra su thay doi tren model tao 1 file migrations
# python manage.py sqlmigrate <Ten app> <number migrations>: xem duoi dang SQL command
# python manage.py migrate: Apply thay doi xuong CSDL
# tao moi 1 bang co ten la <ten app viet thuong >_<ten class model viet thuong>

