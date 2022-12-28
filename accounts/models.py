from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


# Only allow letters, digits
class UsernameValidator(UnicodeUsernameValidator):
    regex = r'^[a-zA-Z0-9]+$'


class CustomUser(AbstractUser):
    username_validator = UsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. May only contain letters and digits.'),
        validators=[username_validator],
        error_messages={
            'unique': _('A user with that username already exists'),
            'invalid': _('Username may only contain letters and digits.')
        },
    )
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


class Friendship(models.Model):

    class Status(models.IntegerChoices):
        PENDING = 0
        ACCEPTED = 1
    
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="friendships_sender")
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="friendships_recipient")
    status = models.IntegerField(choices=Status.choices)
