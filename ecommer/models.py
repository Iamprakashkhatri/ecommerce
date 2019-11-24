from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

class Project(models.Model):
    name=models.CharField(max_length=200)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=300,null=True)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
    role = models.CharField(max_length=300, null=True)
    user1 = models.ForeignKey(Project, on_delete=models.CASCADE)

class Task(models.Model):
    summary = models.CharField(max_length=32)
    content = models.TextField(null=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('assign_task', 'Assign task'),
        )

class Company(models.Model):
    name=models.CharField(max_length=300)

class Site(models.Model):
    name=models.CharField(max_length=300)

class Post(models.Model):
    title = models.CharField('title', max_length=64)
    slug = models.SlugField(max_length=64)
    content = models.TextField('content')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        permissions = (
            ('hide_post', 'Can hide post'),
            ('post_add','Can add post'),
        )
        get_latest_by = 'created_at'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return {'post_slug': self.slug}






























































