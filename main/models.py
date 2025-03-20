from django.db import models
class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True, primary_key=True, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    bio = models.TextField(max_length=100)
class blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField()   
    date = models.DateField(auto_created=True, blank=False, null=False)
    
    