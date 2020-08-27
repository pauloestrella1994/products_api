from django.db import models
import uuid

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    gtin = models.CharField(max_length=14, null=False)
    origin = models.CharField(max_length=16, null=False)
    sku = models.CharField(max_length=16, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    offer = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    approved = models.BooleanField(default=False)
    free_shipping = models.BooleanField(default=False)
    brand = models.CharField(max_length=128, null=False)
    status = models.CharField(max_length=64, null=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    seller_id = models.UUIDField(null=False)
