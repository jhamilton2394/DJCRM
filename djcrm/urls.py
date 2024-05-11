from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordChangeDoneView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path, include
from leads.views import (
    home_page, landing_page, SignupView, LandingPageView)
from leads import urls

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("__reload__/", include("django_browser_reload.urls")),

]
