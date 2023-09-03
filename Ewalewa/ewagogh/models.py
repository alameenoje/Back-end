from django.db import models

class Peeps(models.Model):
    name = models.CharField(max_length=200)
    prompt = models.TextField()

    def __str__(self) -> str:
        return self.name

# Create your models here.
