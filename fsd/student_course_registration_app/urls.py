from django.urls import path

from . import views

urlpatterns = [
path('index/', views.index, name='index'),
path('register-student/', views.register_student, name='register_student'),
path('register-course/', views.register_course, name='register_course'),
path('student-list/<int:course_id>/', views.student_list, name='student_list'),
path('register-project/', views.register_project, name='register_project'),
path('students/', views.StudentListView.as_view(), name='student_list_all'),
path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]
