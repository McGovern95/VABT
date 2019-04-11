from django.db import models
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date_began = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    Certificate_of_eligibility = models.BooleanField(default=False)
    MVP_information_sheet = models.BooleanField(default=False)
    Student_responsibility = models.BooleanField(default=False)

    Resident_tuition_app = models.BooleanField(default=False)
    Concise_student_schedule = models.BooleanField(default=False)
    Star_degree_audit = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.title, self.student)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


        

