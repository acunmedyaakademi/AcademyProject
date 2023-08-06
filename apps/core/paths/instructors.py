from django.urls import path, include
from ..views import instructors

urlpatterns = [
    path('instructor-panel/', include([
            path('', instructors.instructor_panel, name='instructor_panel'),
            path('video/', include([
                path('upload/', instructors.video_upload, name='video_upload'),
                path('edit/<slug:slug>/', instructors.video_edit, name='video_edit'),
                path('delete/<int:pk>/', instructors.video_delete, name='video_delete'),

            ])),
            path('mission/', include([
                path('add/', instructors.mission_add, name='mission_add'),
                path('edit/', instructors.mission_edit, name='mission_edit'),
                path('delete/', instructors.mission_delete, name='mission_delete'),
            ])),
            path('start-lesson/<int:pk>/', instructors.start_lesson, name='start_lesson'),
            path('finish-attendance/<int:pk>/', instructors.finish_attendance, name='finish_attendance'),
        ])),
]