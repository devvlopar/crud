from enum import unique
from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.user_name

class Task(models.Model):
    ALL_CATEGORIES = [
        ('Out Door', 'Out Door'),
        ('In Door', 'In Door')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=35, choices = ALL_CATEGORIES)
    create_date = models.DateTimeField(null=True, blank=True, auto_now_add = True )
    complete_date = models.DateTimeField(null=True, blank=True, auto_now = True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
