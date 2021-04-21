from django.db import models

# Create your models here.
class RegisterModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	password=models.CharField(max_length=24)
	phno=models.IntegerField()

class ContactModel(models.Model):
	YourName=models.CharField(max_length=40)
	YourEmail=models.EmailField()
	YourMessage=models.TextField()


class AddstudentModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	password=models.CharField(max_length=24)
	gender=models.CharField(max_length=30)
	phno=models.IntegerField()
	dob=models.DateField()
	city=models.CharField(max_length=40)
	state=models.CharField(max_length=50)
	pincode=models.IntegerField()
	course=models.CharField(max_length=30)
	add=models.TextField()

	

