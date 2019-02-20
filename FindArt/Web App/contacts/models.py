from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    piece = models.CharField(max_length=200)
    piece_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
    