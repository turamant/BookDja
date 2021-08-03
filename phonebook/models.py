from django.db import models

# Create your models here.
from django.urls import reverse


class Phboo(models.Model):
    name = models.CharField(max_length=100)
    nomer = models.CharField(max_length=12)
    birthday = models.DateField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phonebook_detail', kwargs={'slug': self.url})


