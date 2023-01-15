from django.db import models
from django.contrib.auth.models import AbstractUser
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Newsphoto(models.Model):
    img=models.ImageField(upload_to='news_images/')

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    mini_text = models.TextField()
    img = models.ManyToManyField(Newsphoto,blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE ,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(News, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    reply_comment = models.ForeignKey('BlogComment', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.username
