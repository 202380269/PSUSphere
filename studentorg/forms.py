from django import forms
from .models import Organization, College, Program, Student, OrgMember

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = '__all__'
