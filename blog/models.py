from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User=get_user_model()

class Post(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    active=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='blog/images/',default='blog/images/rein.jpg')
    category=models.ManyToManyField('Category')
    breif_description=models.CharField(max_length=255,null=True,blank=True)
    tags=TaggableManager()
    def __str__(self):
        return self.title 
    class Meta:
        ordering = ['-created_time']



class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    active=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_time']