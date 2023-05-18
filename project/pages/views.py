from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def Add_Student(request):
    name = request.POST.get('name')
    idoCollage = request.POST.get('id')
    dob = request.POST.get('dob')
    gpa = request.POST.get('gpa')
    gender = request.POST.get('gender')
    status = request.POST.get('status')
    department = request.POST.get('department')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    level = request.POST.get('level')

    found_object = None

    for obj in Student.objects.all():
        if obj.idoCollage == idoCollage:
            found_object = obj
            break

    if not found_object:
        std = Student(name=name, idoCollage=idoCollage, level=level, department=department, gender=gender,
                      status=status, dob=dob, gpa=gpa, email=email,
                      mobile=mobile)
        std.save()
        x = {'name': 'The account is successfully added. '}
    else:
        x = {'name': 'Cannot add this Student,This ID is for another student.'}

    return render(request, 'pages/Add Student.html', x)


def update_student_information(request):
    if request.method == 'POST':
        id_of_collage = request.POST.get('id')
        if id_of_collage:  # if the id is not None
            try:
                student = Student.objects.get(idoCollage=id_of_collage) # throw exception if there is no student with this ID
                # check if the user want to delete the student or update his information
                if request.POST.get('action') == 'Delete Student':  # delete the student
                    student.delete()
                    messages.add_message(request, messages.SUCCESS, 'The account has been successfully deleted.')
                    return redirect(to='Update Student Information')

                elif request.POST.get('action') == 'Update Student':  # update the student information
                    if request.POST.get('name'):
                        student.name = request.POST.get('name')
                    if request.POST.get('level'):
                        student.level = request.POST.get('level')
                    if request.POST.get('department'):
                        student.department = request.POST.get('department')
                    if request.POST.get('dob'):
                        student.dob = request.POST.get('dob')
                    if request.POST.get('gpa'):
                        student.gpa = request.POST.get('gpa')
                    if request.POST.get('status'):
                        student.status = True if request.POST.get('status') == 'active' else False
                    if request.POST.get('email'):
                        student.email = request.POST.get('email')
                    if request.POST.get('mobile'):
                        student.mobile = request.POST.get('mobile')
                    student.save()

                    messages.add_message(request, messages.SUCCESS, 'The account has been successfully updated.')
                    return redirect(to='Update Student Information')

            except Student.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'There is no student with this ID.')
                return redirect(to='Update Student Information')

    return render(request, 'pages/Update Student Information.html')


def Assign_Department_Page(request):
    student_id = request.POST.get('student-id')
    department = request.POST.get('department-name')

    try:
        student = Student.objects.get(idoCollage=student_id)

        if student.level == 3:
            student.department = department
            student.save()
            x = {'student_id': student_id, 'message': 'The account has been successfully updated.'}
        else:
            x = {'student_id': student_id, 'message': "You can't update the department for this student."}


    except Student.DoesNotExist:
        x = {'message': 'No student with this ID'}

    return render(request, 'pages/Assign Department Page.html', x)





def Home(request):
    return render(request, 'pages/Home.html')




def Inactive_Students_Page(request):
    if request.method == 'POST':
        status = request.POST.get('status')

        if status == 'active':
            students = Student.objects.filter(status=True)
        elif status == 'inactive':
            students = Student.objects.filter(status=False)

    else:
        students = Student.objects.filter(status=None)
    
    context = {'students': students}

    return render(request, 'pages/Inactive Students Page.html', context)




def Search_For_Students(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        try:
            student = Student.objects.filter(idoCollage=student_id).first()
            if student:
                context = {'student': student}
            else:
                context = {'error_message': "There is no student with this ID."}
        except Student.DoesNotExist:
            context = {'error_message': "There is no student with this ID."}
    else:
        context = {}

    return render(request, 'pages/Search For Students.html',context)




def View_All_Students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'pages/View All Students.html', context)


