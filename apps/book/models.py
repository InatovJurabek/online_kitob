from django.db import models
from apps.common.models import  BaseModel
from  django.contrib.auth.models import AbstractUser



class Books(BaseModel):
        title = models.CharField(max_length=100)
        description = models.TextField(blank=True, null=True)
        author = models.CharField(max_length=100)
        cover = models.ImageField(upload_to='covers/')
        release_year = models.IntegerField()
        category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
        new_column= models.CharField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.IntegerField()
        
        
class CustomUser(AbstractUser):
        phone_number = models.CharField(max_length=20, blank=True, null=True)
        address = models.TextField(blank=True, null=True)
        
        
        
class Category(BaseModel):
        title = models.CharField(max_length=100)
        description = models.TextField()
       
        
        
        
class Publisher(BaseModel):
        publisher = models.ForeignKey(Books, on_delete=models.PROTECT)
        title = models.CharField(max_length=100)
        address = models.CharField(max_length=100)
        description = models.TextField()
        
        
class Cart(BaseModel):
        user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
        book = models.ForeignKey(Books, on_delete=models.CASCADE)
        quantity = models.IntegerField(default=0, blank=True, null=True)
        date_added = models.DateTimeField(auto_now_add=True)
        
        
class Order(BaseModel):
        user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
        status = models.CharField()
        total_price = models.DecimalField(max_digits=10, decimal_places=2)
        
        
        
        
        
        
        
