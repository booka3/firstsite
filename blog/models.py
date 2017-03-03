from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

class BlogDD(models.Model):
    xz = models.TextField()

class MyModel(models.Model):
	fn = models.CharField(max_length=255)
	ln = models.CharField(max_length=255)

admin.site.register(BlogPost, BlogPostAdmin)
