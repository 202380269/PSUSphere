from django.forms import ModelForm
from django import forms
from .models import College, Program, Organization, Student, OrgMember

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class OrganizationMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"