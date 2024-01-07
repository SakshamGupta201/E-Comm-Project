from collections.abc import Iterable
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to="photos/categories")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.category_name

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])
