from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
