from cgi import print_arguments
from email import message
from multiprocessing import context
from re import L
from urllib import request
from django.shortcuts import render, redirect
from Auth_app.models import Staff, Staff_Notification, Staff_leav, Staff_feedback, Subject, Sessin_year, Student, Attendence, Attendence_report, Result
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def Staff_Home(request):
    context= {}
    return render(request, 'Staff/Staff_home.html', context)


@login_required
def Notification(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        notidfication = Staff_Notification.objects.filter(staff_id=staff_id)

        context={
            'notification':notidfication
        }


        return render(request, 'Staff/notification.html', context)
@login_required
def Mark_notification(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notification')

@login_required
def Apply_leav(request):
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id
        staff_leave = Staff_leav.objects.filter(staff_id=staff_id)
   
    context = {
        'staff_leave':staff_leave
    }
    return render(request, 'Staff/staff_apply_leav.html', context)


@login_required
def Staff_Apply_leave_save(request):
    
    if request.method=='POST':
        leave_date = request.POST.get('leave_date')
        leave_massage = request.POST.get('leave_massage')
        staff_id = Staff.objects.get(admin=request.user.id)

        staff_leave = Staff_leav(
            staff_id = staff_id,
            date = leave_date,
            messege = leave_massage
        )
        staff_leave.save()
        messages.success(request, 'You Application successfully send!')
        return redirect('staff_apply_leav')


def Staff_Feefback(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    staff_feedback = Staff_feedback.objects.filter(staff_id=staff_id)
    context = {
        'staff_feedback':staff_feedback
    }

    return render(request, 'Staff/staff_feedback.html', context)


def Staff_save_feedback(request):
    staff = Staff.objects.get(admin=request.user.id)
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

    staff_feedback = Staff_feedback(
        staff_id = staff,
        feedback = feedback,
        reply_feedback = ''
    )
    staff_feedback.save()
    messages.success(request, 'Feedback Successfully send!')
    return redirect('staff_feedback')


def Take_attendance(request):
    staff = Staff.objects.get(admin=request.user.id)
    subejct = Subject.objects.filter(staff=staff)
    session_year = Sessin_year.objects.all()
    
    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Sessin_year.objects.get(id=session_year_id)


            subject = Subject.objects.filter(id=subject_id)

            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(ciurse_id=student_id)
    context = {
        'subejct':subejct,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students
    }
    return render(request, 'Staff/take_attendance.html',context )


def Save_attendance(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Sessin_year.objects.get(id=session_year_id)  

        attendance = Attendence(
            subject_id = get_subject,
            attendance_date = attendance_date,
            sessin_year_id = get_session_year,
        )
        attendance.save()
        for i in student_id:
            stu_id = i
            int_stu = int(stu_id)

            P_student = Student.objects.get(id=int_stu)

            atendance_report = Attendence_report(
                student_id = P_student,
                attendance_id = attendance
            )
            atendance_report.save()
    return redirect('take_attendance')


def view_attendance(request):

    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    session_year = Sessin_year.objects.all()
    action = request.GET.get('action')


    get_subject = None
    get_session_year = None
    attendance_date = None
    atendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Sessin_year.objects.get(id=session_year_id)
            attendance = Attendence.objects.filter(subject_id=get_subject, attendance_date=attendance_date)

            for i in attendance:
                attendance_id = i.id
                atendance_report = Attendence_report.objects.filter(attendance_id=attendance_id)

    context = {
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'atendance_report':atendance_report
    }
    return render(request, 'Staff/view_attendance.html', context)

def Add_result(request):
    staff = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff)
    session_year = Sessin_year.objects.all()
    action = request.GET.get('action')

    get_session_year = None
    get_subject = None
    student = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Sessin_year.objects.get(id=session_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                student = Student.objects.filter(ciurse_id=student_id)
    context = {
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'student':student
    }
    return render(request, 'Staff/add_result.html', context)


def Save_student_rtesult(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)


        check_exists = Result.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exists:
            result = Result.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            messages.success(request, 'Result successfully Updated!')
            return redirect('add_result')
        else:
            result = Result(
                student_id = get_student,
                subject_id = get_subject,
                exam_mark = Exam_mark,
                assignment_mark = assignment_mark
            )

            result.save()
            messages.success(request, 'Result sucessfully added')
            return redirect('add_result')