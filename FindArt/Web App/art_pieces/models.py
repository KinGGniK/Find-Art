from django.db import models
from datetime import datetime
from artists.models import Artist

class Art_Pieces(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  art_type = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%m/%d/')
  is_Sold = models.BooleanField(default=False)
  date_entered = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title