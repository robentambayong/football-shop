from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)           # item name
    price = models.IntegerField()                     # item price
    description = models.TextField()                  # item description
    thumbnail = models.URLField(blank=True, null=True)  # optional image (URL)
    category = models.CharField(max_length=100, blank=True, null=True)  # optional category
    is_featured = models.BooleanField(default=False)  # featured status

    def __str__(self):
        return self.name
