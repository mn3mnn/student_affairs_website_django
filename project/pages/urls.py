from django.urls import path

from . import views

urlpatterns = [
    path('AddStudent', views.Add_Student, name='Add Student'),
    path('AssignDepartmentPage', views.Assign_Department_Page, name='Assign Department Page'),
    path('', views.Home, name='Home'),
    path('InactiveStudentsPage', views.Inactive_Students_Page, name='Inactive Students Page'),
    path('SearchForStudents', views.Search_For_Students, name='Search For Students'),
    path('UpdateStudentInformation', views.update_student_information, name='Update Student Information'),
    path('ViewAllStudents', views.View_All_Students, name='View All Students'),
    path('ChangeStudentStatus', views.change_student_status, name='Change Student Status'),

]
