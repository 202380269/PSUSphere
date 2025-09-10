from django.contrib import admin
from .models import College, Program, Student, Organization, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("id", "college_name", "description")

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "program_name", "college", "description")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "program")

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "college", "description")

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "organization", "position")
