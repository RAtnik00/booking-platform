from accounts.models import CustomUser
from django.shortcuts import render

def tutor_list(request):
    tutors = CustomUser.objects.filter(role='tutor')
    print('TUTORS:', tutors)
    for t in tutors:
        print(t.username, hasattr(t, 'tutor_profile'), t.tutor_profile.subjects)
    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})
