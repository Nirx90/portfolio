from django.db import models

# Create your models here.
class FrontEnd(models.Model):
    field = models.CharField(max_length=100,null=True)
    icon = models.CharField(max_length=100)
    volume = models.IntegerField()

    def __str__(self):
        return self.field

class BackEnd(models.Model):
    field = models.CharField(max_length=100,null=True)
    icon = models.CharField(max_length=100)
    volume = models.IntegerField()

    def __str__(self):
        return self.field
    
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    icon = models.CharField(max_length=150)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    

class Resume(models.Model):
    file = models.FileField(upload_to='files')
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    

