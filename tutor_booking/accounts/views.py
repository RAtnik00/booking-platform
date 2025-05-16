from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, TutorProfileForm, StudentProfileForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def edit_profile_view(request):
    user = request.user

    if user.role == 'tutor':
        profile = user.tutor_profile
        if request.method == 'POST':
            form = TutorProfileForm(request.POST, instance=profile, user=user)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = TutorProfileForm(instance=profile, user=user)

    elif user.role == 'student':
        if request.method == 'POST':
            form = StudentProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = StudentProfileForm(instance=user)

    else:
        return redirect('logout')

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def dashboard_view(request):
    return redirect('edit_profile')

