from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,  PasswordResetConfirmView, PasswordResetCompleteView
from .views import dashboard_view

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', dashboard_view, name='profile'),
    # PASSWORD CHANGE
    path('password-change', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # PASSWORD RESET
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
