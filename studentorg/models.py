from django.db import models

class College(models.Model):
    college_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.college_name


class Program(models.Model):
    program_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.program_name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrgMember(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.student} - {self.organization}"
