from django.db import models
from django.contrib.auth.models import User 
from django.forms import BooleanField, CharField
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from tinymce import models as tinymce_models

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=200, null = True, blank = True)
    description = HTMLField( null = True, blank = True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Coinlist(models.Model):
    COIN_NAME = [('BTC', 'BTCUSDT'),
    ('ETH', 'ETHUSDT'),
    ('BNB', 'BNBUSDT'),
    ('ADA', 'ADAUSDT'),
    ('LTC', 'LTCUSDT'),]

    coinname = models.CharField(max_length=3, choices=COIN_NAME,default="BTC")

    def __str__(self):
        return self.coinname
