from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models import ForeignKey, CharField
from django.utils.text import slugify

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('tutor', 'Tutor'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

class TutorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tutor_profile'
    )
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=255, blank=True, default="")
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    subjects = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
