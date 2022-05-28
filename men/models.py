from django.db import models

# Create your models here.

class Men(models.Model):
    mens_category_name = models.CharField(max_length=50, unique=True)
    # url of category
    mens_slug = models.SlugField(max_length=100, unique=True)
    mens_description = models.TextField(max_length=250, blank=True)
    mens_category_img = models.ImageField(upload_to='photos/category', blank=True)

    def __str__(self):
        return self.mens_category_name
