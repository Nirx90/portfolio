from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20,blank=False,null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name