from django.urls import path, include
from ..views import users
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('profile/', include([
            path('<slug:slug>/', users.profile_detail, name='profile_detail'),
            path('', users.profile, name='profile'),
        ])),
        path('profile-update/', users.profile_update, name='profile_update'),
        path('favorites/', include([
            path('', users.favorite_videos, name='favorite_videos'),
            path('add/<slug:slug>/', users.favorite_video, name='add_favorite_video'),
            path('delete/<slug:slug>/', users.favorite_video, name='delete_favorite_video'),
        ])),
        path('auth/', include([
            path('first-login/', users.first_login_page, name='first_login'),
            path('first-login-validate/', users.first_login_validate, name='first_login_validate'),
            path('force-password-change/', users.force_password_change, name='force_password_change'),
            path('login/', auth_views.LoginView.as_view(template_name='user/users/login.html'), name='login'),
            path('logout/', auth_views.LogoutView.as_view(), name='logout'),
            path('password', include([
                path('change/', auth_views.PasswordChangeView.as_view(template_name='user/users/password_change.html'),
                     name='password_change'),
                path('reset/', include([
                    path('', auth_views.PasswordResetView.as_view(template_name='user/users/password_reset.html'),
                         name='password_reset'),
                    path('done/',
                         auth_views.PasswordResetDoneView.as_view(template_name='user/users/password_reset_done.html'),
                         name='password_reset_done'),
                    path('confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                        template_name='user/users/password_reset_confirm.html'), name='password_reset_confirm'),
                    path('complete/', auth_views.PasswordResetCompleteView.as_view(
                        template_name='user/users/password_reset_complete.html'), name='password_reset_complete'),
                ])),
            ])),
        ])),

]
