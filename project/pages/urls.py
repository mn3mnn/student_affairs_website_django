from django.urls import path

from . import views

urlpatterns = [
    path('AddStudent', views.add_student, name='Add Student'),
    path('AssignDepartmentPage', views.assign_department, name='Assign Department Page'),
    path('', views.home, name='Home'),
    path('InactiveStudentsPage', views.active_inactive_students, name='Active/Inactive Students'),
    path('SearchForStudents', views.search_for_students, name='Search For Students'),
    path('UpdateStudentInformation', views.update_student_information, name='Update Student Information'),
    path('ViewAllStudents', views.view_all_students, name='View All Students'),
    path('ChangeStudentStatus', views.change_student_status, name='Change Student Status'),

]
