from django.db import models
from category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="photos/product")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name
