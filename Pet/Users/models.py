from django.db import models
from django_ulid.models import default, ULIDField


class Users(models.Model):
    """       this is model for users    """
    id_user = models.AutoField(primary_key=True)  # id of Users
    firstname = models.CharField(max_length=255)  # firstname of users
    lastname = models.CharField(max_length=255)  # last name of users
    username = models.CharField(max_length=255)  # username of users
    password = models.CharField(max_length=255)  # password of users
    phone = models.CharField(max_length=12)  # phone number of users
    add_date = models.DateTimeField(auto_now_add=True)  # date the users join

    def __str__(self):
        return self.username + '         ' + str(self.add_date)
