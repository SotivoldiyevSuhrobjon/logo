from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} -  {self.description}"

class Service(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title}"


class Clien(models.Model):
    img = models.ImageField(upload_to='clien', blank=True, null=True)
    description = models.TextField()
    title = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title} - {self.description}"


class Make(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} -  {self.email}"
