from django.urls import path
from .views import tutor_list, tutor_detail, my_bookings

urlpatterns = [
    path('tutors/', tutor_list, name='tutor_list'),
    path('tutors/<slug:slug>/', tutor_detail, name='tutor_detail'),
    path('my-bookings/', my_bookings, name='my_bookings')
]