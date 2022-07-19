from unicodedata import category
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to="resumes/" , blank=True, null=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    is_public = models.BooleanField(default=False)
    

    def __str__(self):
        return self.username


    def get_absolute_url(self):
          return reverse('signup-step2', args=[str(self.id)])


    
    
    




