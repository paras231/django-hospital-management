from django.db import models

# Create your models here.


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    age  =  models.IntegerField()
    email =  models.TextField(unique=True)
    mobile  = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name