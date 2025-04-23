from accounts.models import CustomUser
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from datetime import datetime

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
    tutor = get_object_or_404(CustomUser, slug=slug, role='tutor')

    if request.method == 'POST':
        print('--- POST received ---')
        datetime_value = request.POST.get('datetime')
        print('datetime from form:', datetime_value)
        print('user:', request.user.username)
        print('role:', getattr(request.user, 'role', None))

        if request.user.is_authenticated and getattr(request.user, 'role', None) == 'student':
            try:
                datetime_obj = datetime.strptime(datetime_value, "%Y-%m-%dT%H:%M")
                Booking.objects.create(
                    student=request.user,
                    tutor=tutor,
                    datetime=datetime_obj,
                    status='pending'
                )
                print('✅ Booking created')
                return HttpResponseRedirect(request.path_info)
            except Exception as e:
                print('❌ Error during booking:', e)

    context = {'tutor': tutor}
    return render(request, 'tutors/tutor_detail.html', context)

def my_bookings(request):
    if not request.user.is_authenticated:
        return  redirect('tutor_list')

    if request.user.role == 'student':
        bookings = Booking.objects.filter(student=request.user)
    elif request.user.role == 'tutor':
        bookings = Booking.objects.filter(tutor=request.user)
    else:
        bookings = Booking.objects.none()

    return render(request, 'tutors/my_bookings.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user.is_authenticated and request.user.role == 'student' and booking.student == request.user:
        booking.status = 'cancelled'
        booking.save()

    return HttpResponseRedirect('/my-bookings/')

def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user.is_authenticated and request.user.role == 'tutor' and booking.tutor == request.user:
        booking.status = 'confirmed'
        booking.save()

    return HttpResponseRedirect('/my-bookings/')