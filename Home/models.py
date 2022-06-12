from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    time_stamp = datetime.date.today()
    def __str__(self) -> str:
        return self.title
