from django.db import models

# Create your models here.
class Songs(models.Model):
    name= models.CharField(null=True,max_length=200)
    song = models.FileField(upload_to='songs/')
    songimage = models.FileField(upload_to='images/')
    artist=models.CharField(null=True,max_length=200)
    def __str__(self) -> str:
        return self.name + " " + str(self.id)