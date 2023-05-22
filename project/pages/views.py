from django.shortcuts import render, redirect
from .models import Student
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


def add_student(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            id_of_college = request.POST.get('id')
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
                if obj.idoCollage == id_of_college:
                    found_object = obj
                    break

            if not found_object:
                std = Student(name=name, idoCollage=id_of_college, level=level, department=department, gender=gender,
                              status=status, dob=dob, gpa=gpa, email=email,
                              mobile=mobile)
                std.save()
                return JsonResponse({"msg": 'The student has been added successfully.'}, status=200)
            else:
                return JsonResponse({"msg": 'There is another student with the same ID.'}, status=400)

        except Exception as e:
            print(e)
            return JsonResponse({"msg": 'Cannot add this Student.'}, status=400)

    return render(request, 'pages/Add Student.html')


def update_student_information(request):
    if request.method == 'POST':
        id_of_collage = request.POST.get('id')
        if id_of_collage:  # if the id is not None
            try:
                student = Student.objects.get(idoCollage=id_of_collage) # throw exception if there is no student with this ID
                # check if the user want to delete the student or update his information

                if request.POST.get('action') == 'delete':  # delete the student
                    student.delete()
                    return JsonResponse({"msg": "The account has been successfully deleted."}, status=200)

                elif request.POST.get('action') == 'update':  # update the student information
                    if request.POST.get('isSearch') == 'true':
                        # serialize in new student object in json
                        ser_instance = serializers.serialize('json', [student, ])
                        # send to client side.
                        return JsonResponse({"std": ser_instance}, status=200)

                    # else update student data
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
                        student.status = True if request.POST.get('status') == '1' else False
                    if request.POST.get('email'):
                        student.email = request.POST.get('email')
                    if request.POST.get('mobile'):
                        student.mobile = request.POST.get('mobile')
                    student.save()

                    return JsonResponse({"msg": 'The account has been successfully updated.'}, status=200)

            except Exception as e:
                return JsonResponse({"msg": 'There is no student with this ID.'}, status=400)

    return render(request, 'pages/Update Student Information.html')


def change_student_status(request):
    if request.method == 'POST':
        id_of_college = request.POST.get('std_id')
        if id_of_college:
            std = Student.objects.get(idoCollage=id_of_college)
            if std:
                curr_status = std.status
                std.status = not curr_status
                std.save()
                return JsonResponse({"msg": 'The status has been successfully updated.',
                                     "new_status": 'active' if std.status else 'inactive',
                                     "old_status": 'active' if curr_status else 'inactive'}, status=200)
            else:
                return JsonResponse({"msg": 'There is no student with this ID.'}, status=400)

    return render(request, 'pages/Change Student Status.html')


def assign_department(request):
    if request.method == 'POST':

        student_id = request.POST.get('student-id')
        department = request.POST.get('department-name')

        try:
            student = Student.objects.get(idoCollage=student_id)
            student.department = department if department != 'None' else None
            student.save()
            return JsonResponse({'msg': 'The department has been assigned successfully.'}, status=200)

        except Student.DoesNotExist:
            return JsonResponse({'msg': 'No student with this ID'}, status=400)

    return render(request, 'pages/Assign Department Page.html')


def home(request):
    return render(request, 'pages/Home.html')


def active_inactive_students(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        students = None
        if status == 'active':
            students = Student.objects.filter(status=True)

        elif status == 'inactive':
            students = Student.objects.filter(status=False)

        if students:
            # serialize in new student object in json
            ser_instance = serializers.serialize('json', students)
            # send to client side.
            return JsonResponse({"std": ser_instance}, status=200)
        else:
            return JsonResponse({"msg": 'There is no student with this status.'}, status=400)

    return render(request, 'pages/Inactive Students Page.html')


def search_for_students(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        student_name = request.POST.get('name')

        if student_id:  # search by id if it is not None
            try:
                student = Student.objects.get(idoCollage=student_id)
                if student:
                    # serialize in new student object in json
                    ser_instance = serializers.serialize('json', [student, ])
                    # send to client side.
                    return JsonResponse({"std": ser_instance}, status=200)

            except Student.DoesNotExist:
                return JsonResponse({"msg": 'No student with this ID.'}, status=400)

        elif student_name:  # search by name if the id is None and the name is not None
            try:
                students = Student.objects.filter(name__contains=student_name)
                if students:
                    # serialize in new student object in json
                    ser_instance = serializers.serialize('json', students)
                    # send to client side.
                    return JsonResponse({"std": ser_instance}, status=200)
                else:
                    return JsonResponse({"msg": 'No students with this name.'}, status=400)

            except Student.DoesNotExist:
                return JsonResponse({"msg": 'No students with this name.'}, status=400)

    return render(request, 'pages/Search For Students.html')


def view_all_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'pages/View All Students.html', context)


