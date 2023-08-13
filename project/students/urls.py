from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_student, name='addStudent'),
    path('assign', views.assign_department, name='assignDepartmentPage'),
    path('search', views.search_for_students, name='searchForStudents'),
    path('update', views.update_student_information, name='updateStudentInformation'),
    path('all', views.view_all_students, name='viewAllStudents'),
    path('changeStatus', views.change_student_status, name='changeStudentStatus'),
    path('student/<std_id>', views.student_info, name='studentInfo'),

]
