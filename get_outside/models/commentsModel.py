import uuid
from random import randrange

from django.db import models
from authentication.models import CustomUser
from get_outside.models.mappointModel import Mappoint


def key_generator():
    key = randrange(100, 100000)
    if CustomUser.objects.filter(id=key).exists():
        key = key_generator()
    return key


class Comment(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.IntegerField(primary_key=True, default=key_generator, unique=True)
    mappoint_id = models.ForeignKey(Mappoint, related_name='comments', default=0, on_delete=models.CASCADE)
    author_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)  # oder SET() ???
    created_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text
