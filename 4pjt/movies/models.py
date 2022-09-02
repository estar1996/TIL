from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #제한이 없는 녀석

    def _str_(self):
        return self.title