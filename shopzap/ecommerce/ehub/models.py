from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=300)
    productdetails=models.TextField()
    productprize=models.FloatField()
    productimage=models.ImageField(null=True)
    productcategory=models.CharField(max_length=30,null=True,blank=True)
    
    class Meta:
        ordering=["-productprize"]

    def __str__(self):
        return self.productname

class fashion(models.Model):
    productname=models.CharField(max_length=300)
    productdetails=models.TextField()
    productprize=models.FloatField()
    productimage=models.ImageField(null=True)
    productcategory=models.CharField(max_length=30,null=True,blank=True)
class test(models.Model):
    productname=models.CharField(max_length=300)
    productdetails=models.TextField()
    productprize=models.FloatField()
    productimage=models.ImageField(null=True)
    productcategory=models.CharField(max_length=30,null=True,blank=True)

