from django.db import models
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class chapter(models.Model):
    form_coe = models.BooleanField(default=False)
    form_info = models.BooleanField(default=False)
    form_resp = models.BooleanField(default=False)
    form_resident = models.BooleanField(default=False)
    form_concise = models.BooleanField(default=False)
    form_starda = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_published:
            self.draft = False
        if self.draft:
            self.published = False
        super().save(*args, **kwargs)


        

