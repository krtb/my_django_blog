from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # link to another model
    title = models.CharField(max_length=200) #define text with limited amount of characters
    text = models.TextField() #long text with out limit
    create_date = models.DateTimeField(default=timezone.now) 