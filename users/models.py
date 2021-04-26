from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):

    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
