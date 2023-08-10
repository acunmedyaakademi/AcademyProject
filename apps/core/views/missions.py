from django.shortcuts import render, get_object_or_404
from apps.core.models import Users, MissionModel, MissionSubmissionsModel
from ..forms.missions import MissionCompleteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def missions_page(request):
    classroom = request.user.classroom.first()
    missions = classroom.missions.all()
    return render(request, 'user/missions/list.html', {
        'missions': missions,
        'classroom': classroom
    })


def mission_detail(request, slug):
    mission = get_object_or_404(MissionModel, slug=slug)
    check_user_submission = MissionSubmissionsModel.objects.filter(mission=mission, student=request.user).exists()
    mission_students = mission.classroom.users.filter(groups__name='Öğrenci')
    if request.method == 'POST':
        if check_user_submission:
            user_submission = MissionSubmissionsModel.objects.get(mission=mission,
                                                                  student=request.user)
            form = MissionCompleteForm(request.POST, instance=user_submission)
        else:
            form = MissionCompleteForm(request.POST)
        if form.is_valid():
            mission_complete = form.save(commit=False)
            mission_complete.mission = mission
            mission_complete.student = request.user
            mission_complete.save()
            messages.success(request, 'Görev başarıyla tamamlandı')
    else:
        if check_user_submission:
            form = MissionCompleteForm(instance=request.user)
            user_submission = MissionSubmissionsModel.objects.get(mission=mission,
                                                                             student=request.user)
            form.initial['url'] = user_submission.url
        else:
            form = MissionCompleteForm()
    return render(request, 'user/missions/detail.html', {
        'mission': mission,
        'form': form,
        'mission_students': mission_students
    })
