from django.db import models

# Create your models here.
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)