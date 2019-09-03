from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from phone_field import PhoneField


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    address = models.CharField(max_length=255, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username', 'first_name', 'last_name', 'address', 'phone'
    ]

    def __str__(self):
        return "{}".format(self.email)


# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE,
#                                 related_name='profile')
#     title = models.CharField(max_length=5)
#     dob = models.DateField()
#     address = models.CharField(max_length=255)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zip = models.CharField(max_length=5)
#     photo = models.ImageField(upload_to='uploads', blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='Teacherprofile')
    subjectexprty = models.CharField(max_length=255)
    YearOfExp = models.IntegerField(default=0)


# class Student(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE,
#                                 related_name='profile')
#     YearOfExp = models.IntegerField(default=0)
