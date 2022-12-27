from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/', default='images/blank-profile-picture-g603ac37a8_640_pzvogy.png')
    slug = models.SlugField(blank=True, null=True)

    # Code to generate a default from field in the same model
    # from Elf Sternberg on StackOverflow (https://stackoverflow.com/a/4381252)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        if not self.display_name:
            self.display_name = self.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
