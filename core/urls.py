from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='home'),
    path('students/', core.views.Students.as_view(), name='students_list'),
    path('curators/', core.views.Curators.as_view(), name='curators_list'),
    path('students/<int:pk>/', core.views.StudentDetail.as_view(), name='students_detail'),
    path('curators/<int:pk>/', core.views.CuratorDetail.as_view(), name='curators_detail'),
]
