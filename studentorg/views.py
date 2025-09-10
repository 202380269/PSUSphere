from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organization, College, Program, Student, OrgMember
from .forms import OrganizationForm, CollegeForm, ProgramForm, StudentForm, OrgMemberForm

# Home Page
class HomePageView(ListView):
    model = Organization
    template_name = "home.html"
    context_object_name = "home"


# Organization
class OrganizationList(ListView):
    model = Organization
    template_name = "org_list.html"
    context_object_name = "object_list"

class OrganizationCreate(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')

class OrganizationUpdate(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')

class OrganizationDelete(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy('organization-list')


# College
class CollegeList(ListView):
    model = College
    template_name = "college_list.html"

class CollegeCreate(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy('college-list')

class CollegeUpdate(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy('college-list')

class CollegeDelete(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy('college-list')


# Program
class ProgramList(ListView):
    model = Program
    template_name = "program_list.html"

class ProgramCreate(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy('program-list')

class ProgramUpdate(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy('program-list')

class ProgramDelete(DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy('program-list')


# Student
class StudentList(ListView):
    model = Student
    template_name = "student_list.html"

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student-list')

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student-list')

class StudentDelete(DeleteView):
    model = Student
    template_name = "student_del.html"
    success_url = reverse_lazy('student-list')


# OrgMember
class OrgMemberList(ListView):
    model = OrgMember
    template_name = "orgmember_list.html"

class OrgMemberCreate(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdate(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDelete(DeleteView):
    model = OrgMember
    template_name = "orgmember_del.html"
    success_url = reverse_lazy('orgmember-list')
