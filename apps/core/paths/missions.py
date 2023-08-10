from django.urls import path, include
from ..views import missions

urlpatterns = [
    path('missions/', include([
        path('', missions.missions_page, name='missions_list'),
        path('<slug:slug>/', missions.mission_detail, name='mission_detail'),
    ])),
]
