from django.db import models

# Create your models here.
class AddingBooksOrDVDs(models.Model):
    Author=models.CharField(max_length=200, default="author")
    Title=models.CharField(max_length=35, default="title")
    Date=models.CharField(max_length=10, default="dd-mm-yyyy")
    Picture=models.TextField(default="picture")
