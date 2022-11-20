from django.db import models

from products.models import Product


class Requests(models.Model):
    title = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)