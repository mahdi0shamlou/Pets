from django.db import models
from Animals.models import Animals

class Vaccines(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=400, unique=True)
    age = models.IntegerField()
    type = models.ForeignKey(Animals, null=False, on_delete=models.CASCADE)

