from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from Auth_app.models import Student, Student_Notification, Student_feedback, Student_leav, Subject, Attendence, Attendence_report, Result 

def Student_home(request):
    return render(request, 'Student/home.html')



def Notification(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id=student_id)
        context = {
            'notification':notification
        }
        return render(request, 'Student/notification.html', context)

def mark_notification(request, status):
    notification = Student_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('student_notification')

def Student_feedback_show(request):
    student_id = Student.objects.get(admin=request.user.id)

    student_feedback = Student_feedback.objects.filter(student_id=student_id)
    context = {
        'student_feedback':student_feedback
    }
    return render(request, 'Student/feedback.html', context)

def Student_save_feedback(request):
    student = Student.objects.get(admin=request.user.id)
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

    feedback = Student_feedback(
        student_id = student,
        feedback = feedback,
        reply_feedback = ''
    )
    feedback.save()
    messages.success(request, 'Feedback send successfully!')
    return redirect('student_feedback')

def Student_leave_apply(request):
    student_id1 = Student.objects.filter(admin=request.user.id)

    for i in student_id1:
        student_id = i.id
        student_leave = Student_leav.objects.filter(student_id=student_id)
    context = {
        'student_leave':student_leave
    }
    return render(request, 'Student/stu_apply_leave.html',context)

def student_leave_save(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_massage = request.POST.get('leave_massage')
        student_id = Student.objects.get(admin=request.user.id)

        student_leave = Student_leav(
            student_id = student_id,
            date = leave_date,
            messege = leave_massage,
        )
        student_leave.save()
        messages.success(request, 'Apply aplication successfully send!')

        return redirect('student_leave')


def Student_view_attendance(request):
    student_id = Student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course=student_id.ciurse_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('suject_id')
            get_subject = Subject.objects.get(id=subject_id)
            attendance_report = Attendence_report.objects.filter(student_id=student_id, attendance_id__subject_id=subject_id)
    context = {
        'subject':subject,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report
    }
    return render(request, 'Student/view_attendance.html', context)

def Student_view_result(request):
    student = Student.objects.get(admin=request.user.id)
    result = Result.objects.filter(student_id=student)
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        total = assignment_mark + exam_mark
    context = {
        'result':result,
        'total':total
    }
    return render(request, 'Student/view_result.html',context )