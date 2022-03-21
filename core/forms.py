from django import forms

import core.models


class StudentsEdit(forms.ModelForm):
    class Meta:
        model = core.models.Students
        fields = '__all__'


class CuratorsEdit(forms.ModelForm):
    class Meta:
        model = core.models.Curator
        fields = '__all__'
