from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)  # item name
    price = models.IntegerField()            # item price
    description = models.TextField()         # item description
    thumbnail = models.URLField()            # item image (URL)
    category = models.CharField(max_length=100)  # item category
    is_featured = models.BooleanField(default=False)  # featured status

    def __str__(self):
        return self.name