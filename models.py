from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=20)
    city = models.CharField(max_length=20)
    course_enrolled = models.CharField(max_length=20)
    enrollment_date = models.DateField(max_length=20)

    def __str__(self):
        return self.student_name
