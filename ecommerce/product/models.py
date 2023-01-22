from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField()
  parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class CustomizationOption(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  categories = models.ManyToManyField(Category)
  availability = models.BooleanField(default=True)
  stock = models.IntegerField()
  images = models.ImageField(upload_to="products/")
  customization_options = models.ManyToManyField(CustomizationOption)

