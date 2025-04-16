from accounts.models import CustomUser
from django.shortcuts import render, get_object_or_404

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
    context = {'tutor': tutor}
    return  render(request, 'tutors/tutor_detail.html', context)