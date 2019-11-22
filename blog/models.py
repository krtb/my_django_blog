from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # link to another model
    title = models.CharField(max_length=200) #define text with limited amount of characters
    text = models.TextField() #long text with out limit
    created_date = models.DateTimeField(default=timezone.now) 
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self): 
        #use dudner for str, "double underscore"
        #consider changing __str__ to __unicode__
        return self.title