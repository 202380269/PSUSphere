"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, a path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentorg.views import (
    HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    OrgMemberList, OrgMemberCreateView, OrgMemberDeleteView, OrgMemberUpdateView,
    StudentCreateView, StudentDeleteView, StudentList, StudentUpdateView,
    CollegeCreateView, CollegeDeleteView, CollegeList, CollegeUpdateView,
    ProgramCreateView, ProgramDeleteView, ProgramList, ProgramUpdateView,
    GlobalSearchListView
)
from studentorg import views


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # 🔑 Authentication (Login, Signup, Logout, Password reset via django-allauth)
    path("accounts/", include("allauth.urls")),

    # Home
    path('', views.HomePageView.as_view(), name='home'),
    path("index.html/", views.HomePageView.as_view(), name="index"),

    # Change this path to use the new GlobalSearchListView
    path("search/", GlobalSearchListView.as_view(), name="global_search"),

    # Organization
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # Organization Member
    path('organizationMember_list/', OrgMemberList.as_view(), name='organization-member-list'),
    path('organizationMember_list/add/', OrgMemberCreateView.as_view(), name='organization-member-add'),
    path('organizationMember_list/<pk>/', OrgMemberUpdateView.as_view(), name='organization-member-update'),
    path('organizationMember_list/<pk>/delete/', OrgMemberDeleteView.as_view(), name='organization-member-delete'),

    # Student
    path('student_list/', StudentList.as_view(), name='student-list'),
    path('student_list/add/', StudentCreateView.as_view(), name='student-add'),
    path("student_list/<pk>/", StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # College
    path('college_list/', CollegeList.as_view(), name='college-list'),
    path('college_list/add/', CollegeCreateView.as_view(), name='college-add'),
    path("college_list/<pk>/", CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Program
    path('program_list/', ProgramList.as_view(), name='program-list'),
    path('program_list/add/', ProgramCreateView.as_view(), name='program-add'),
    path("program_list/<pk>/", ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),
]