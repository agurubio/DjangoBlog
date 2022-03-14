from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    descripcion = models.TextField()
    web_link = models.URLField(max_length=200)
    def __str__(self):
        return f"Usuario: {self.user}"
   
class Avatar(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'avatares', blank= True)
    def __str__(self):
        return f"Avatar - {self.user}"