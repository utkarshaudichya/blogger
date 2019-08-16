from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class PermanentAddress(models.Model):
    user = models.OneToOneField(User, related_name='permanent_address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=32, default='')
    state = models.CharField(max_length=32, default='')
    pincode = models.CharField(max_length=10, default='')
    country = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.street_address+' '+self.city+' '+self.state+' '+self.pincode+' '+self.country

class CorrespondenceAddress(models.Model):
    user = models.OneToOneField(User, related_name='correspondence_address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=32, default='')
    state = models.CharField(max_length=32, default='')
    pincode = models.CharField(max_length=10, default='')
    country = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.street_address+' '+self.city+' '+self.state+' '+self.pincode+' '+self.country

class Profile(models.Model):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    profile_pic = models.ImageField(blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png'])])
    birth_date = models.DateField(blank=True, null=True)
    permanent_address = models.OneToOneField(PermanentAddress, on_delete=models.CASCADE, related_name='permanent')
    correspondence_address = models.OneToOneField(CorrespondenceAddress, on_delete=models.CASCADE, related_name='correspondence')
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return self.user.username
