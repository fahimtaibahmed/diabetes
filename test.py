from django.db import models

class Person(models.Model): 
    Name = models.CharField(max_length=30)