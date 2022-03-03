from django.shortcuts import render
import core.models


def index(request):
    students = core.models.Students.objects.all()
    return render(request, 'core/index.html', {'students': students})
