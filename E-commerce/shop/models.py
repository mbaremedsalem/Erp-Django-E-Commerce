from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models import F
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser   


# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     city = models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE, blank=True, null=True)
#     phone_number = models.CharField(max_length=15)
#     image = models.ImageField(upload_to='profile/')
#     def __str__(self):
#         return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='jobs/')
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name
        
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    pourcatange = models.FloatField(blank=True, null=True)
    pricenet = models.FloatField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category ,related_name='category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs/')
    date_added = models.DateTimeField(auto_now=True) 

    slug = models.SlugField(blank=True, null=True)
    
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.title 
    def save(self, *args, **kwargs):
        self.pricenet = self.price * self.pourcatange
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs) 
          

class Order(models.Model):
    product = models.ForeignKey(Product,related_name='apply_order',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)   


    class Meta:
        ordering = ['-date_added']      
    def __str__(self):
        return self.name 


# class User(AbstractUser):
#        is_simple_user = models.BooleanField(default=False)
       

# class user(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True) 
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.user.username        