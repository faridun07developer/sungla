from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.


class Sungla(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sunDetailView', args=[self.slug])


class About(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    status = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)
    view_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('aboutDetailView', args=[self.slug])

    def __str__(self):
        return self.name


class Haqida(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    status = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('haqidaDetailView', args=[self.slug])

    def __str__(self):
        return self.name


class Carusel(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    img = models.ImageField(upload_to=200)
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('caruselDetailView', args=[self.slug])

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField()
    massage = models.TextField()
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    products = models.ForeignKey(About,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"


class Foydalanuvchi(models.Model):
    jinsi = models.BooleanField(max_length=50)
    ismi = models.CharField(max_length=200)
    yosh = models.IntegerField()

    def __str__(self):
        return self.ismi

# git init
# git add *
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/faridun07developer/sungla.git
# git push -u origin main