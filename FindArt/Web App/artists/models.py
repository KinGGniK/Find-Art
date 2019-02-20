from django.db import models
from datetime import datetime

# Create your models here.
class Artist(models.Model):
    full_name = models.CharField(max_length=150)
    art_type = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    date_entered = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='photos/%m/%d/')

    def __str__(self):
        return self.full_name 
