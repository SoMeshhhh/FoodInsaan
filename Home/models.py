from django.db import models

# Create your models here.


class FoodIssine(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name
