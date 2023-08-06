from django.shortcuts import render
from apps.core.models import Users, MissionModel
from django.contrib.auth.decorators import login_required


@login_required()
def missions_page(request):
    classroom = request.user.classroom.first()
    missions = classroom.missions.all()
    return render(request, 'user/missions/list.html', {
        'missions': missions,
        'classroom': classroom
    })