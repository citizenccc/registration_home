from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.title} --> {self.description}"
