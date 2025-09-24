from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from .models import Organization, College, Program, Student, OrgMember
from .forms import OrganizationForm, CollegeForm, ProgramForm, StudentForm, OrganizationMemberForm

# Home Page
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values("student")
            .distinct()
            .count()
        )
        context["students_joined_this_year"] = count
        return context

# Organization Views
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ["name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "college__college_name"

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# OrgMember Views
class OrganizationMemberList(ListView):
    model = OrgMember
    context_object_name = 'organizationmember'
    template_name = 'org_member_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(student__student_id__icontains=query) |
                Q(student__lastname__icontains=query) |
                Q(student__firstname__icontains=query) |
                Q(student__middlename__icontains=query) |
                Q(student__program__prog_name__icontains=query) |
                Q(organization__name__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ["student__lastname", "student__firstname", "organization__name", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student__lastname"

class OrganizationMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('organization-member-list')

class OrganizationMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('organization-member-list')

class OrganizationMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmem_del.html'
    success_url = reverse_lazy('organization-member-list')

# Student Views
class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(student_id__icontains=query) |
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) |
                Q(middlename__icontains=query) |
                Q(program__prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ["lastname", "firstname", "student_id", "program__prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "lastname"

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

# College Views
class CollegeListView(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

    def get_ordering(self):
        allowed = ["college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "college_name"

class CollegeCreateView(CreateView):
    model = College
    fields = '__all__'
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    fields = '__all__'
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# Program Views
class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"

class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')