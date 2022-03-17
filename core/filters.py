import django_filters

import core.models


class Student(django_filters.FilterSet):
    second_name = django_filters.Filter(lookup_expr='istartswith')

    class Meta:
        model = core.models.Students
        fields = ('second_name', 'direction',)


class Curator(django_filters.FilterSet):
    second_name = django_filters.Filter(lookup_expr='istartswith')

    class Meta:
        model = core.models.Curator
        fields = ('second_name', 'department',)
