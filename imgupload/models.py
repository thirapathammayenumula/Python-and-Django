from django.db import models
from django.utils import timezone

# Create your models here.
class ImgModel(models.Model):
    iname=models.CharField(max_length=100,blank=False,null=True)
    images=models.ImageField(upload_to="Images/",blank=False,null=True)
    flag=models.CharField(max_length=2,default=0,choices=(('0','0'),('1','1')),blank=False,null=True)
    def __str__(self):
         return self.iname