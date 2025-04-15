from accounts.models import CustomUser
from django.shortcuts import render, get_object_or_404

def tutor_list(request):
    tutors = CustomUser.objects.filter(role='tutor')
    print('TUTORS:', tutors)
    for t in tutors:
        print(t.username, hasattr(t, 'tutor_profile'), t.tutor_profile.subjects)
    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})

def tutor_detail(request, slug):
    tutor = get_object_or_404(CustomUser, slug=slug, role = 'tutor')
    context = {'tutor': tutor}
    return  render(request, 'tutors/tutor_detail.html', context)