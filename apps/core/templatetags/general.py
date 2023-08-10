from django import template
from apps.core.models import Users, Videos, MissionSubmissionsModel
from django.template.defaultfilters import stringfilter
import re
from urllib.parse import urlparse

register = template.Library()


@register.simple_tag()
def students_count():
    students = Users.objects.filter(groups__name='Öğrenci')
    return students.count()


@register.simple_tag()
def instructors_count():
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return instructors.count()


@register.filter(name='usermention', is_safe=True)
@stringfilter
def usermention(value):
    value = re.sub(r'@(\w+)', r'<a class="text-blue-800" href="/\1/">@\1</a>', value)
    return value


@register.simple_tag()
def videos_count():
    videos = Videos.objects.all()
    return videos.count()


@register.filter(name='video_embed')
@stringfilter
def video_embed(value):
    url_data = urlparse(value)
    query = urlparse(url_data.query)
    url = query.path.replace('v=', '')
    return 'https://youtube.com/embed/' + url


@register.filter(name='check_student_submission')
def check_student_submission(student, mission):
    return MissionSubmissionsModel.objects.filter(mission=mission, student=student).exists()

@register.filter(name='get_submission_info')
def get_submission_info(student, mission):
    return MissionSubmissionsModel.objects.get(mission=mission, student=student) if MissionSubmissionsModel.objects.filter(mission=mission, student=student).exists() else 'Tamamlanmadı'
