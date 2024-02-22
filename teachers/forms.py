from django import forms
from .models import Teacher, Lecture


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name"]

class LecturesForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ["name", "theme", "teacher"]



class ContactForm(forms.Form):
    field1 = forms.CharField(label="Poličko 1", max_length=10)
    field2 = forms.IntegerField(label="Poličko 2")


