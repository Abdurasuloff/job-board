from datetime import date
from django.db import models
from django.urls import reverse
from accounts.models import User
from job.models import Category

# Create your models here.



class Resume(models.Model):
      title = models.CharField(max_length=100, null=True, blank=True)
      owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_owner')
      category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
      description = models.CharField(max_length=170, null=True, blank=True)
      date = models.DateTimeField(auto_now_add=True)
      url = models.CharField(max_length=100, null=True, blank=True)
      cost = models.PositiveIntegerField(default=0)
      cost_for = models.CharField(max_length=50, blank=True, null=True )


      def __str__(self):
        return self.owner.username

      def get_absolute_url(self):
        return reverse('index')

class Hire(models.Model):
      resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume', null=True, blank=True) 
      worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker-hire+')
      employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employer-hire+', null=True, blank=True )
      about_company = models.TextField(null=True, blank=True)
      massage = models.TextField(null=True, blank=True)
      date = models.DateTimeField(auto_now_add=True)
      status = models.CharField(max_length=70, default="In Progress")
      new = models.BooleanField(default=True)
      deleted = models.BooleanField(default=False)
  

      def __str__(self):
        return self.worker.username

      def get_absolute_url(self):
        return reverse('index')