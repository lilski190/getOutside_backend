import uuid
from random import random, randrange

from django.contrib.auth.models import AbstractUser
from django.db import models


def key_generator():
    key = randrange(100, 100000)
    if CustomUser.objects.filter(id=key).exists():
        key = key_generator()
    return key


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'profile_pictures/{filename}'.format(filename=filename)


class CustomUser(AbstractUser):
    id = models.IntegerField(primary_key=True, default=key_generator, unique=True)
    fav_activity = models.CharField(blank=True, max_length=120)
    profile_picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
