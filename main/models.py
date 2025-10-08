from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    # Add this line to fix the error
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

