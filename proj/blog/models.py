from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class POST(models.Model):
    status = [
        (0, 'Draft'),
        (1, 'Publish')
    ]

    title = models.CharField(max_length=200, null=True, help_text='Enter Your Title', verbose_name='Post Title')
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    post_status = models.IntegerField(choices=status, default=0)
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
