from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,  PasswordResetConfirmView, PasswordResetCompleteView
from .views import dashboard_view, user_register, SignUpView, edit_user, EditUserView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', dashboard_view, name='profile'),
    #     path('profile/edit', edit_user, name='edit_user_information'),
    path('profile/edit', EditUserView.as_view(), name='edit_user_information'),
    path('signup', user_register, name='user_register'),
    #     path('signup', SignUpView.as_view(), name='user_register'),
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
