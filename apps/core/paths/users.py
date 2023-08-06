from django.urls import path, include
from ..views import users
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth/', include([
        path('first-login/', users.first_login_page, name='first_login'),
        path('first-login-validate/', users.first_login_validate, name='first_login_validate'),
        path('force-password-change/', users.force_password_change, name='force_password_change'),
        path('login/', auth_views.LoginView.as_view(template_name='user/users/login.html'), name='login'),
        path('password-change/', auth_views.PasswordChangeView.as_view(template_name='user/users/password_change.html'), name='password_change'),
        path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/users/password_reset.html'), name='password_reset'),
        path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/users/password_reset_done.html'), name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/users/password_reset_confirm.html'), name='password_reset_confirm'),
        path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/users/password_reset_complete.html'), name='password_reset_complete'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ])),
    path('users/', include([
        path('profile/', users.profile, name='profile'),
        path('profile/update/', users.profile_update, name='profile_update'),
        path('favorite_video/<slug:slug>/', users.favorite_video, name='favorite_video'),
        path('favorite-videos/', users.favorite_videos, name='favorite_videos'),
    ]))
]