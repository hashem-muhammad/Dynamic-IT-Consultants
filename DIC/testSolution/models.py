from django.db import models
from django.contrib.auth.models import AbstractUser

from testSolution.Manager.UserManager import UserManager
# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, null=True)

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.email}'


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.URLField()
    details = models.TextField()
    country = models.CharField(max_length=4, null=True)
    published_date = models.DateTimeField(null=True)
    language = models.CharField(max_length=4, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
