from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.list_student, name="list_student"),
    path("register/", views.register_student, name="register_student"),
    path("delete_student/<student_id>", views.delete_student, name="delete_student"),
    path("update_student/<student_id>", views.update_student, name="update_student"),
    path("update/uprec/<student_id>", views.uprec, name="uprec"),

]
