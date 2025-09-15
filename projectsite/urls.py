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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView,OrganizationUpdateView, OrganizationDeleteView, OrganizationMemberList, OrganizationMemberCreateView, OrganizationMemberDeleteView, OrganizationMemberUpdateView, StudentCreateView, StudentDeleteView, StudentListView, StudentUpdateView, CollegeCreateView, CollegeDeleteView, CollegeListView, CollegeUpdateView, ProgramCreateView, ProgramDeleteView, ProgramListView, ProgramUpdateView
from studentorg import views
from django.views.generic import TemplateView
from django.contrib.sites.models import Site

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', views.HomePageView.as_view(), name='home'),
    path("index.html", views.HomePageView.as_view(), name="index"), 
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('organizationMember_list', OrganizationMemberList.as_view(), name='organization-member-list'),
    path('organizationMember_list/add', OrganizationMemberCreateView.as_view(), name='organization-member-add'),
    path('organizationMember_list/<pk>', OrganizationMemberUpdateView.as_view(), name='organization-member-update'),
    path('organizationMember_list/<pk>/delete', OrganizationMemberDeleteView.as_view(), name='organization-member-delete'),
    path('student_list', StudentListView.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'), 
    path("student_list/<pk>", StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'), 
    path('college_list', CollegeListView.as_view(), name='college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path("college_list/<pk>", CollegeUpdateView.as_view(), name='college-update'),  
    path('college_list/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),
    path('program_list', ProgramListView.as_view(), name='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name='program-add'),
    path("program_list/<pk>", ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete', ProgramDeleteView.as_view(), name='program-delete'), 
]