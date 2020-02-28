from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.id
