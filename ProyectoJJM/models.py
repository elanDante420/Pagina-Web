from django.db import models

# Create your models here.

class UserCreator(models.Model):
    playername = models.CharField(max_length=200) # Nickname
    username = models.CharField(max_length=200) # Usuario
    userpassword = models.CharField(max_length=200) # Clave
    usernumber = models.CharField(max_length=20)  # Tlf
    useremail = models.EmailField()  # Correo
    playerclass = models.TextField()  # clase
    
    
    def __str__(self):
        return self.correo