from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='home'),
    path('students/', core.views.Students.as_view(), name='students_list'),
    path('students/<int:pk>/', core.views.StudentDetail.as_view(), name='students_detail'),
    path('students/create/', core.views.StudentsCreate.as_view(), name='students_create'),
    path('students/<int:pk>/update/', core.views.StudentsUpdate.as_view(), name='students_update'),
    path('students/<int:pk>/delete/', core.views.StudentsDelete.as_view(), name='students_delete'),
    path('curators/', core.views.Curators.as_view(), name='curators_list'),
    path('curators/<int:pk>/', core.views.CuratorDetail.as_view(), name='curators_detail'),
    path('curators/create/', core.views.CuratorCreate.as_view(), name='curators_create'),
    path('curators/<int:pk>/update/', core.views.CuratorUpdate.as_view(), name='curators_update'),
    path('curators/<int:pk>/delete/', core.views.CuratorDelete.as_view(), name='curators_delete'),
]
