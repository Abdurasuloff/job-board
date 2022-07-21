from random import choices
from django.db import models
from accounts.models import User


# Create your models here.



class Massage(models.Model):
      sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
      receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
      body = models.CharField(max_length=1000, null=True, blank=True)
      file = models.FileField(upload_to='massage_files/', null=True, blank=True )
      is_seen = models.BooleanField(default=False)
      date = models.DateTimeField(auto_now_add=True)

