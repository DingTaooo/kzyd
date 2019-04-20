from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # id = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Books(models.Model):
    bookId = models.CharField(max_length=32, primary_key=True)
    bookname = models.CharField(max_length=32)
    author = models.CharField(max_length=64)
    intro = models.CharField(max_length=256)