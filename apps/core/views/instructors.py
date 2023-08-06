from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.core.decorators import group_required
from apps.core.forms.instructor_forms import VideoUpload, MissionForm
from django.contrib import messages
from apps.core.models import Users
from django.conf import settings
from apps.core.models import Classroom, AttendanceModel, Lessons
import requests
from django.http import QueryDict


@login_required()
def instructor_list(request):
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return render(request, 'user/instructors/list.html', {
        'instructors': instructors
    })


@login_required()
@group_required('Eğitmen')
def instructor_panel(request):
    classrooms = request.user.classroom.all()
    videos = request.user.instructor_videos.all().order_by('-id')[:5]
    return render(request, 'user/instructors/instructor_panel.html', {
        'videos': videos,
        'classrooms': classrooms
    })


@login_required()
@group_required('Eğitmen')
def start_lesson(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    students = classroom.users.filter(groups__name='Öğrenci')
    if request.method == 'POST':
        new_lesson = Lessons.objects.create(instructor=request.user, classroom=classroom)
        selected_students = request.POST.getlist('student')
        new_attendance = AttendanceModel.objects.create(lesson=new_lesson)
        for student_id in selected_students:
            new_attendance.student.add(student_id)
        return redirect('finish_attendance', pk=new_attendance.pk)
    return render(request, 'user/instructors/start_lesson.html', {
        'students': students
    })


@login_required()
@group_required('Eğitmen')
def finish_attendance(request, pk):
    attendance = get_object_or_404(AttendanceModel, pk=pk)
    return render(request, 'user/instructors/finish_attendance.html', {
        'attendance': attendance
    })


@login_required()
@group_required('Eğitmen')
def mission_add(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.instructor = request.user
            mission.save()
            messages.success(request, 'Görev başarıyla oluşturuldu')
            return redirect('homepage')
    else:
        form = MissionForm()
    return render(request, 'user/instructors/add_mission.html', {
        'form': form
    })


@login_required()
@group_required('Eğitmen')
def mission_delete(request):
    pass

@login_required()
@group_required('Eğitmen')
def mission_edit(request):
    pass


@login_required()
@group_required('Eğitmen')
def video_upload(request):
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            video = form.save(commit=False)
            video.instructor = request.user
            video.save()
            messages.success(request, 'Video başarıyla yüklendi')
            return redirect('instructor_panel')
    else:
        form = VideoUpload(user=request.user)
    return render(request, 'user/instructors/video_upload.html', {
        'form': form
    })


@login_required()
@group_required('Eğitmen')
def video_edit(request, slug):
    video = request.user.instructor_videos.get(slug=slug)
    if request.method == 'POST':
        form = VideoUpload(request.POST, request.FILES, user=request.user, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video başarıyla güncellendi')
            return redirect('instructor_panel')
    else:
        form = VideoUpload(user=request.user, instance=video)
    return render(request, 'user/instructors/video_edit.html', {
        'form': form
    })


@login_required()
@group_required('Eğitmen')
def video_delete(request, pk):
    request_video = request.user.instructor_videos.get(pk=pk)
    url = "https://storage.bunnycdn.com/" + settings.BUNNY_USERNAME + "/" + request_video.video_file.name
    url = url.replace("\\", "/")
    headers = {"AccessKey": settings.BUNNY_PASSWORD}
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        video = request.user.instructor_videos.get(pk=pk)
        video.delete()
        messages.success(request, 'Video başarıyla silindi')
        return redirect('instructor_panel')
    else:
        messages.error(request, 'Video silinirken bir hata oluştu')
        return redirect('instructor_panel')
