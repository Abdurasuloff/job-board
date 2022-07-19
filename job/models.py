from unicodedata import category, name
from django.db import models
from django.forms import SlugField
from accounts.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
      name = models.CharField(max_length=150)
      slug = models.SlugField()

      def __str__(self):
        return self.name


class Vacancy(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      title = models.CharField(max_length=150)
      description = models.TextField()
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      cost = models.PositiveIntegerField()
      cost_for = models.CharField(max_length=50)
      work_type = models.CharField(max_length=50)
      is_closed = models.BooleanField(default=False)
      location = models.CharField(max_length=150)
      needed_experience = models.CharField(max_length=100)
      tags = models.CharField(max_length=150, null=True, blank=True)
      company_name = models.CharField(max_length=150 , blank=True, null=True)
      tagline = models.CharField(max_length=300 , blank=True, null=True)
      company_email = models.CharField(max_length=100, blank=True, null=True)
      company_logo = models.ImageField(upload_to="company_logos/",  blank=True, null=True)
      date = models.DateField(auto_now_add=True)
      #number of sended applications to this vacancy
      applications = models.PositiveIntegerField(default=0)
      deleted = models.BooleanField(default=False)

      def __str__(self):
        return self.title

      def get_absolute_url(self):
        return reverse('manage-vacancies')

class Apply(models.Model):
      vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True )
      worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker')
      employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employer', null=True, blank=True )
      new = models.BooleanField(default=True)
      resume = models.FileField(upload_to='massage_files/', null=True, blank=True )
      massage = models.TextField(null=True, blank=True)
      date = models.DateTimeField(auto_now_add=True)
      status = models.CharField(max_length=70, default="In Progress")
      deleted = models.BooleanField(default=False)
      edited = models.BooleanField(default=False)

      def __str__(self):
        return self.vacancy.title

      def get_absolute_url(self):
        return reverse('index')

      

