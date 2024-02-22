from django.http import HttpResponse
from django.template import loader
from .models import Teacher
from django.shortcuts import render, redirect
from .forms import TeacherForm, ContactForm, LecturesForm

"""
def test_template(request):
    template = loader.get_template("first_template.html")
    #return HttpResponse("Hello Teachers")
    return HttpResponse(template.render())"""


def home_page(request):
    template = loader.get_template("home_page.html")
    #return HttpResponse("Hello Teachers")
    return HttpResponse(template.render())

def teachers(request):
    my_teachers = Teacher.objects.all().values()
    template = loader.get_template("all_teachers.html")
    context = {
        "my_teachers": my_teachers,
    }
    return HttpResponse(template.render(context, request))


def teacher_detail(request, id):
    my_teacher = Teacher.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {
        "my_teacher": my_teacher,
    }
    return HttpResponse(template.render(context, request))


def handler404(request, exception):
    #response = render(template_name)
    template = loader.get_template("404.html")
    #response.status_code = 404
    return HttpResponse(template.render(), status=404)


def teacher_form(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teachers")

    else:
        form = TeacherForm()

    return render(request, "teacher_form.html", {"form": form})

def Lectures_Form(request):
    if request.method == "POST":
        form = LecturesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lectures")

    else:
        form = LecturesForm()

    return render(request, "lectures_form.html", {"form": form})


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # tu spracujem data
            field1 = form.cleaned_data["field1"]
            print("HERE: ", field1)

            return redirect("home_page")

    else:
        form = ContactForm()

    return render(request, "contact_form.html", {"form": form})


