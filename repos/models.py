from django.db import models

# Create your models here.

class Repo(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    title       = models.CharField(max_length=100, blank=True, default='')
    url         = models.CharField(max_length=100, blank=True, default='')
    user_name   = models.CharField(max_length=100, blank=True, default='')
    repo_name   = models.CharField(max_length=100, blank=True, default='')
    branch      = models.CharField(max_length=100, blank=True, default='')
    
    class Meta: 
        ordering = ('created',)
