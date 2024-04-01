from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    phone = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    subjects_taught = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profile/',null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Teachers(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    subjects_taught = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profile/',null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        verbose_name = "Teachers"  # Change the singular name displayed in the admin panel
        verbose_name_plural = "Teachers"
