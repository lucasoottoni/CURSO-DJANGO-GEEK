from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE
    )
    age = models.PositiveSmallIntegerField(_("age"))
    gender = models.CharField(_("gender"), max_length=20)
    married = models.BooleanField(_("married"))