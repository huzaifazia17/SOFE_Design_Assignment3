from django.db import models

class Products(models.Model):
    productCode = models.CharField(max_length=10)
    productName = models.CharField(max_length=50)
    productPrice = models.FloatField(default=0)
    
    class  Meta:
        verbose_name_plural = "Products"

class Purchases(models.Model):
    productCode = models.CharField(max_length=10, default='NULL')
    productName = models.CharField(max_length=50, default='NULL')
    productPrice = models.CharField(max_length=50, default='NULL')
    totalPayment = models.FloatField(default=0)
    
    class  Meta:
        verbose_name_plural = "Purchases"
