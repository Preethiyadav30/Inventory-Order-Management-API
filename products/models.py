from django.db import models
from categories.models import Category

# Create your models here.

class products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    decription=models.TextField(blank=True)
    stock=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )