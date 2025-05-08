from accounts.models import CustomUser
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from datetime import datetime
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required, tutor_required
from django.utils import timezone
from django.utils.timezone import make_aware

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
                naive_dt = datetime.strptime(datetime_value, "%Y-%m-%dT%H:%M")
                datetime_obj = make_aware(naive_dt)

                if datetime_obj > timezone.now():
                    Booking.objects.create(
                        student=request.user,
                        tutor=tutor,
                        datetime=datetime_obj,
                        status='pending'
                    )
                    print('✅ Booking created')
                    return HttpResponseRedirect(request.path_info)
                else:
                    print('❌ Attempt to book past date')
                    return HttpResponseRedirect(f"{request.path_info}?error=past_date")

            except Exception as e:
                print('❌ Error during booking:', e)

    context = {'tutor': tutor}
    return render(request, 'tutors/tutor_detail.html', context)

@login_required(login_url='/accounts/login/')
def my_bookings(request):
    if not request.user.is_authenticated:
        return redirect('tutor_list')

    if request.user.role == 'student':
        bookings = Booking.objects.filter(student=request.user)
    elif request.user.role == 'tutor':
        bookings = Booking.objects.filter(tutor=request.user)
    else:
        bookings = Booking.objects.none()

    status_filter = request.GET.get('status')
    if status_filter in ['pending', 'confirmed', 'cancelled']:
        bookings = bookings.filter(status=status_filter)

    return render(request, 'tutors/my_bookings.html', {'bookings': bookings})


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user.is_authenticated and request.user.role == 'student' and booking.student == request.user:
        booking.status = 'cancelled'
        booking.save()

    return HttpResponseRedirect('/my-bookings/')

@login_required(login_url='/accounts/login/')
@tutor_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user.is_authenticated and request.user.role == 'tutor' and booking.tutor == request.user:
        booking.status = 'confirmed'
        booking.save()

    return HttpResponseRedirect('/my-bookings/')

def home_view(request):
    return render(request, 'tutors/home.html')
