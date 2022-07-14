from django.db import models
from django.contrib.auth.models import User 
from django.forms import BooleanField, CharField
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=200, null = True, blank = True)
    description = models.TextField(max_length=1000000, null = True, blank = True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']