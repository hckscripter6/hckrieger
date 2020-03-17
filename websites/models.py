from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Website(models.Model):
    organization = models.CharField(max_length=150, null=True)
    url = models.URLField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to="websites", null=True, blank=True)
    
    def __str__(self):
        return self.organization