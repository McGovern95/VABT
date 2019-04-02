from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator
# Create your models here.
#extended default User model
#usage: make sure you import from users.models import UserExtended 
#   ex = UserExtended.objects.get(user=request.user) ~ this line gets the fields 
    #ex.chapter ~ this is the chapter field
    #ex.is_student ~ is the boolean for is_student
    #ex.is_firsttime ~ boolean for first time
class UserExtended(models.Model):
    #fields for checking 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chapter = models.CharField(max_length=4,choices=[('33','33'), ('30','30'), ('31','31'),('35','35'),('1606','1606')],blank=True)
    is_firsttime = models.BooleanField(default=True)
    is_student = models.BooleanField(default=True)

    #saves file to a userid directory
    def user_directory_path(instance, filename):
        return 'students/{0}_{1}/{2}'.format(instance.user.last_name,instance.user.first_name,filename)

    ###all files for first time peeps
    cert_of_elig = models.FileField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null=True)
    MVP_info_sheet = models.FileField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null = True)
    stud_respon = models.FileField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null = True)
    resid_tuit_app = models.FileField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null = True)
    #everyone else usually
    conc_stud_sched = models.FileField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null = True)
    star_deg_audit = models.FileField(upload_to=user_directory_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],blank=True,null = True)

    def __str__(self):
        return f'{self.user.username} Extended Student Fields'

    #def save(self, *args,**kwargs):
    #    super(UserExtended,self).save(*args,**kwargs)


class Profile(models.Model): #one to one
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


