from django.db import models
from Users.models import UserData


class Animals(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AnimalsUsers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # name of pets not type of them
    age = models.IntegerField()
    type = models.ForeignKey(Animals, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(UserData, null=False, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + '  :  ' + str(self.type) + ' ------- > ' + self.name


