from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    student = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='student_booking')
    tutor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='tutor_booking')
    datetime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.student.username} -> {self.tutor.username} @ {self.datetime}"
