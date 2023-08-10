from django import forms
from ..models import MissionModel, Classroom, MissionSubmissionsModel
from django.utils.translation import gettext_lazy as _


class MissionCompleteForm(forms.ModelForm):
    class Meta:
        model = MissionSubmissionsModel
        fields = ('url',)
