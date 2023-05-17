from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Student


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



def Update_Student_Information(request):
    idoCollage = request.POST.get('id')
    found_object = None

    for obj in Student.objects.all():
        if obj.idoCollage == idoCollage:
            found_object = obj
            break

    if not found_object:
        x = {'name': 'Not Found.'}
    else:
        x = {'name': 'Found.'}

    return render(request, 'pages/Update Student Information.html', x)



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

