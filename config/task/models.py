from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    bol = models.BooleanField(null=True)



    def __str__(self):
        return self.title



