from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField(blank = False)
    email = models.EmailField(max_length = 100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)