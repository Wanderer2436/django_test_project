from django.shortcuts import render, get_object_or_404
import core.models
from django.views.generic import TemplateView, ListView, DetailView
import core.forms
import core.filters


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'


class Students(TitleMixin, ListView):
    template_name = 'core/students.html'
    title = 'Список студентов'

    def get_filters(self):
        return core.filters.Student(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filters'] = self.get_filters()
        # context['form'] = core.forms.StudentSearch(self.request.GET)
        return context

    def get_queryset(self):
        return self.get_filters().qs


class Curators(TitleMixin, ListView):
    template_name = 'core/curators.html'
    title = 'Список кураторов'

    def get_filters(self):
        return core.filters.Curator(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filters'] = self.get_filters()
        return context

    def get_queryset(self):
        return self.get_filters().qs


class StudentDetail(TitleMixin, DetailView):
    template_name = 'core/students_detail.html'
    title = 'Детальная информация'
    model = core.models.Students


class CuratorDetail(TitleMixin, DetailView):
    template_name = 'core/curators_detail.html'
    title = 'Детальная информация'
    model = core.models.Curator
