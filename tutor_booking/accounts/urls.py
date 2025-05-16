from django.urls import path
from .views import register_view, dashboard_view, edit_profile_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('edit-profile/', edit_profile_view, name='edit_profile'),
]
