from django.db import models
from django.conf import settings
# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='static/images/users', blank=True)
    companyname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return 'Profile for user{}'.format(self.user.username)