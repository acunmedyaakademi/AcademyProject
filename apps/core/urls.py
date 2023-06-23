from django.urls import path, include
from .views import users, main, instructors, videos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include([
        path('', main.homepage, name='homepage'),
        path('login/', auth_views.LoginView.as_view(template_name='user/users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('profile/', users.profile, name='profile'),
        path('issues/', main.issues, name='issues'),
        path('instructor-panel/', include([
            path('', instructors.instructor_panel, name='instructor_panel'),
            path('video-upload/', instructors.video_upload, name='video_upload'),
        ])),
        path('videos/', include([
            path('<int:pk>/', videos.video_detail, name='video_detail'),
        ])),
    ])),
]
