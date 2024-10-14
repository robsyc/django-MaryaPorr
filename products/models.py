from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/imgs/')
    stripe_product_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name