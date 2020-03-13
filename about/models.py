from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    content = RichTextField()
    
    class Meta:
        verbose_name_plural = 'About'
        
    def __str__(self):
        return 'Content for about page'

# Create your models here.
