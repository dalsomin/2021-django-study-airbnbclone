
#
# # Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMAILE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE , "male"),
        (GENDER_FEMAILE , "female"),
        (GENDER_OTHER , "other"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)

