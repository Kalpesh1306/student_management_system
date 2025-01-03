from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

def register_student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        email_id = request.POST.get("email_id")
        contact_number = request.POST.get("contact_number")
        date_of_birth = request.POST.get("date_of_birth")
        city = request.POST.get("city")
        course_enrolled = request.POST.get("course_enrolled")
        enrollment_date = request.POST.get("enrollment_date")


        # Check for duplicate email
        if Student.objects.filter(email_id=email_id).exists():
            messages.error(request, "Email ID already exists!")
            return redirect("register_student")

        # Create and save new students
        Student.objects.create(
            student_name=student_name,
            email_id=email_id,
            contact_number=contact_number,
            date_of_birth=date_of_birth,
            city=city,
            course_enrolled =course_enrolled,
            enrollment_date =enrollment_date,
        )
        messages.success(request, "Students registered successfully!")
        return redirect("register_student")

    return render(request, "student_management_system/register.html")

def list_student(request):
    students = Student.objects.all()  # Retrieve all students
    return render(request, "student_management_system/list.html", {"students": students})

def delete_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    messages.success(request, "Students deleted successfully!")
    return redirect("list_student")

def update_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, "student_management_system/update.html", {"student": student})

def uprec(request, student_id):
    id = request.POST['student_id']
    name = request.POST['student_name']
    email = request.POST['email_id']
    contact = request.POST['contact_number']
    city = request.POST['city']
    course_enrolled = request.POST['course_enrolled']
    student = Student.objects.get(pk=id)
    student.name = name
    student.email_id = email
    student.contact_number = contact
    student.city = city
    student.course_enrolled = course_enrolled
    student.save()
    messages.success(request, "Students updated successfully!")
    return redirect("list_student")


