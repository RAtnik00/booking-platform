from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from .models import TutorProfile


@receiver(post_save, sender=CustomUser)
def create_tutor_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'tutor':
        TutorProfile.objects.create(user=instance)
