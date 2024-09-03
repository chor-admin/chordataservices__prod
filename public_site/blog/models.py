from django.db import models
from django.conf import settings
from PIL.Image import core

class BlogStartTag(models.Model):
  name = models.CharField(max_length=40)

  class Meta:
        app_label = "blog"
        db_table = u'"django_data\".\"blog__start_tag"'
        ordering = ['name']

  def __str__(self):
      return self.name

class BlogStartPost(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(BlogStartTag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        app_label = "blog"
        db_table = u'"django_data\".\"blog__start_post"'
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class BlogRunTag(models.Model):
  name = models.CharField(max_length=40)

  class Meta:
        app_label = "blog"
        db_table = u'"django_data\".\"blog__run_tag"'
        ordering = ['name']

  def __str__(self):
      return self.name

class BlogRunPost(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(BlogRunTag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        app_label = "blog"
        db_table = u'"django_data\".\"blog__run_post"'
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class BlogExitTag(models.Model):
  name = models.CharField(max_length=40)

  class Meta:
        app_label = "blog"
        db_table = u'"django_data\".\"blog__exit_tag"'
        ordering = ['name']

  def __str__(self):
      return self.name

class BlogExitPost(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(BlogExitTag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        app_label = "blog"
        db_table = u'"django_data\".\"blog__exit_post"'
        ordering = ['-created_on']

    def __str__(self):
        return self.title