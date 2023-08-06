from django.urls import path, include
from .views import users, main, instructors, videos, missions
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include([
        path('', include('apps.core.paths.main')),
        # USER URLS
        path('', include('apps.core.paths.users')),
        # INSTRUCTOR URLS
        path('', include('apps.core.paths.instructors')),
        # VIDEOS URLS
        path('', include('apps.core.paths.videos')),
        # MISSIONS URLS
        path('', include('apps.core.paths.missions')),
    ])),
]
