from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import TutorProfile

User = get_user_model()

class TutorProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="jan_kowalski",
            password="securepass123",
            role="tutor"
        )

    def test_tutor_profile_created_via_signal(self):
        profile = TutorProfile.objects.get(user=self.user)
        self.assertEqual(profile.user.username, "jan_kowalski")
        self.assertEqual(profile.price_per_hour, None)

