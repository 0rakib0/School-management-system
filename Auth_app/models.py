from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT')
    )
    User_type = models.CharField(choices=USER , max_length=20, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.course_name

class Sessin_year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.session_start + ' To ' + self.session_end


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    ciurse_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Sessin_year, on_delete=models.DO_NOTHING)
    create_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.admin.first_name


class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.admin.first_name + " " + self.admin.last_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.subject_name

class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    messege = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return self.staff_id.admin.first_name



class Staff_leav(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date  = models.CharField(max_length=100)
    messege = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name

class Staff_feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    reply_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.staff_id.admin.first_name + ' ' + self.staff_id.admin.last_name



class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    messege = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return self.student_id.admin.first_name
    
class Student_feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    reply_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student_id.admin.first_name + ' ' + self.student_id.admin.last_name



class Student_leav(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date  = models.CharField(max_length=100)
    messege = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student_id.admin.first_name + self.student_id.admin.last_name


class Attendence(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    sessin_year_id = models.ForeignKey(Sessin_year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject_id.subject_name


class Attendence_report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.NOT_PROVIDED)
    attendance_id = models.ForeignKey(Attendence, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name


class Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.student_id.admin.first_name