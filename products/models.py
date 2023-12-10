from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    material = models.CharField(max_length=256)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return f'Продукт: {self.name}'