from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView,
    OrganizationList, OrganizationCreate, OrganizationUpdate, OrganizationDelete,
    CollegeList, CollegeCreate, CollegeUpdate, CollegeDelete,
    ProgramList, ProgramCreate, ProgramUpdate, ProgramDelete,
    StudentList, StudentCreate, StudentUpdate, StudentDelete,
    OrgMemberList, OrgMemberCreate, OrgMemberUpdate, OrgMemberDelete,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    # Organization
    path('organizations/', OrganizationList.as_view(), name='organization-list'),
    path('organizations/add/', OrganizationCreate.as_view(), name='organization-add'),
    path('organizations/<int:pk>/', OrganizationUpdate.as_view(), name='organization-update'),
    path('organizations/<int:pk>/delete/', OrganizationDelete.as_view(), name='organization-delete'),

    # College
    path('colleges/', CollegeList.as_view(), name='college-list'),
    path('colleges/add/', CollegeCreate.as_view(), name='college-add'),
    path('colleges/<int:pk>/', CollegeUpdate.as_view(), name='college-update'),
    path('colleges/<int:pk>/delete/', CollegeDelete.as_view(), name='college-delete'),

    # Program
    path('programs/', ProgramList.as_view(), name='program-list'),
    path('programs/add/', ProgramCreate.as_view(), name='program-add'),
    path('programs/<int:pk>/', ProgramUpdate.as_view(), name='program-update'),
    path('programs/<int:pk>/delete/', ProgramDelete.as_view(), name='program-delete'),

    # Student
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/add/', StudentCreate.as_view(), name='student-add'),
    path('students/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDelete.as_view(), name='student-delete'),

    # OrgMember
    path('orgmembers/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmembers/add/', OrgMemberCreate.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/', OrgMemberUpdate.as_view(), name='orgmember-update'),
    path('orgmembers/<int:pk>/delete/', OrgMemberDelete.as_view(), name='orgmember-delete'),
]
