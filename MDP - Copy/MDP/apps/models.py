from django.db import models



class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    feedback = models.TextField()

# Create your models here.
