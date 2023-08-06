from django.urls import path, include
from ..views import videos

urlpatterns = [
    path('videos/', include([
            path('', videos.videos_list, name='videos_list'),
            path('<slug:slug>/', videos.video_detail, name='video_detail'),
            path('comments/create/', videos.video_comment_create, name='video_comment_create'),
            path('comments/delete/<int:pk>/', videos.video_comment_delete, name='video_comment_delete'),
            path('comments/update/<int:pk>/', videos.video_comment_update, name='video_comment_update'),
        ])),
]