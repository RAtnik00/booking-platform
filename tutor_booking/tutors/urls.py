from django.urls import path
from .views import tutor_list

urlpatterns = [
    path('tutors/', tutor_list, name='tutor_list'),
]