from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
