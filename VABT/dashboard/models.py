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
    last_certifier = models.CharField(max_length=80,default='None')
    student = models.ForeignKey(User, related_name='certs', on_delete=models.CASCADE)

    date_cert = models.DateTimeField(default=timezone.now)
    Certificate_of_eligibility = models.BooleanField(default=False)

    date_info = models.DateTimeField(default=timezone.now)
    MVP_information_sheet = models.BooleanField(default=False)


    date_respo = models.DateTimeField(default=timezone.now)
    Student_responsibility = models.BooleanField(default=False)

    date_tuition = models.DateTimeField(default=timezone.now)
    Resident_tuition_app = models.BooleanField(default=False)

    date_concise = models.DateTimeField(default=timezone.now)
    Concise_student_schedule = models.BooleanField(default=False)

    date_audit = models.DateTimeField(default=timezone.now)
    Star_degree_audit = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.title, self.student)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


        

