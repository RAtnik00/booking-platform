from accounts.models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Booking

def tutor_list(request):
    filters = {}
    subject = request.GET.get('subject')
    if subject:
        filters['tutor_profile__subjects__icontains'] = subject

    max_price = request.GET.get('max_price')
    if max_price:
        filters['tutor_profile__price_per_hour__lte'] = max_price

    q = request.GET.get('q')
    if q:
        filters['username__icontains'] = q

    tutors = CustomUser.objects.filter(role='tutor', **filters)

    print('FILTERS:', filters)
    print('TUTORS:', tutors)

    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})

def tutor_detail(request, slug):
    tutor = get_object_or_404(CustomUser, slug=slug, role = 'tutor')

    if request.method == 'POST':
        datetime_value = request.POST.get('datetime')
        if request.user.is_authenticated and request.user.role == 'student':
            Booking.objects.create(
                student=request.user,
                tutor=tutor,
                datetime=datetime_value,
                status='pending'
            )
            return HttpResponseRedirect(request.path_info)

    context = {'tutor': tutor}
    return  render(request, 'tutors/tutor_detail.html', context)