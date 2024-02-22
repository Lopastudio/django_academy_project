from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("teachers/", views.teachers, name="teachers"),
    path("teachers/teachers_form", views.teacher_form, name="teachers_form"),
    path("teachers/lectures_form", views.Lectures_Form, name="Lectures_Form"),
    path("contact", views.contact_form, name="contact_form"),
    path("lectures/", views.teachers, name="lectures"),
    #path("test/", views.test_template, name="test"),
    path("teachers/detail/<int:id>", views.teacher_detail, name="detail"),
]