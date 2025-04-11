from accoutns.moduls import CustomUser
from django.shortcuts import render

def tutor_list(request):
    tutors = CustomUser.objects.filter(role='tutor')
    context = {'tutor': tutors}
    return render(request, 'tutors/tutor_list.html', context)