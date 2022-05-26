from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    text = models.TextField(max_length=600)
    image = models.ImageField(blank = True,upload_to='blog/assets')
    def __str__(self):
        return self.title
