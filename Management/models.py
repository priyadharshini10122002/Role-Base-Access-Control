from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=50)
    provider=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
   
    def __str__(self):
         return f"{self.title}"    

