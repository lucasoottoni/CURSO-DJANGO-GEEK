from django.db import models
#from django.utils.translation import gettext_lazy as _
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 


# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User, 
#         verbose_name=_("user"), 
#         on_delete=models.CASCADE
#     )
#     age = models.PositiveSmallIntegerField(_("age"))
#     gender = models.CharField(_("gender"), max_length=20)
#     married = models.BooleanField(_("married"))
class User(AbstractUser):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_IN_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_IN_CHOICES, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=120, null=True, blank=True)
    is_approved_to_be_in_touch = models.BooleanField(default=False)