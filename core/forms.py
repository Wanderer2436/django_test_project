from django import forms

import core.models


# class StudentSearch(forms.Form):
#     second_name = forms.CharField(label='Фамилия', required=False)
#     direction = forms.CharField(label='Направление', required=False)
#
#     def clean_second_name(self):
#         second_name = self.cleaned_data.get('second_name')
#
#         if second_name and not str(second_name).isalpha():
#             raise forms.ValidationError('Фамилия не может содержать числа!')
#
#         return second_name
#
#
# class CuratorsSearch(forms.Form):
#     second_name = forms.CharField(label='Фамилия', required=False)
#     department = forms.CharField(label='Кафедра', required=False)


class StudentsEdit(forms.ModelForm):
    class Meta:
        model = core.models.Students
        fields = '__all__'



