from distutils.log import log
from multiprocessing import context
from traceback import print_tb
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Auth_app.models import Course, Sessin_year, CustomUser, Student, Staff, Subject, Staff_Notification, Staff_leav, Staff_feedback, Student_Notification, Student_feedback, Student_leav, Attendence, Attendence_report
from django.contrib import messages

@login_required
def hod(request):
    student = Student.objects.all().count()
    staff = Staff.objects.all().count()
    course = Course.objects.all().count()
    subject = Subject.objects.all().count()
    Male_student = Student.objects.filter(gender='Male').count()
    Female_student = Student.objects.filter(gender='Femal').count()
    diction = {
        'student':student,
        'staff':staff,
        'course':course,
        'subject':subject,
        'Male_student':Male_student,
        'Female_student':Female_student,
    }
    return render(request,'Hod/home.html', context=diction)

@login_required
def add_student(request):
    course = Course.objects.all()
    session_year = Sessin_year.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')
        address = request.POST.get('address')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already taken!')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Already taken!')
            return redirect('add_student')

        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                User_type = 3

            )

            user.set_password(password)
            user.save()

            course_id = Course.objects.get(id=course_id)
            session_year = Sessin_year.objects.get(id=session_id)

            student = Student(
                admin = user,
                address = address,
                gender = gender,
                ciurse_id = course_id,
                session_year_id = session_year
            )

            student.save()
            messages.success(request, user.first_name + ' ' + user.last_name + " are Successfully added")
            return redirect('add_student')




    diction = {
        'course':course,
        'session_year':session_year
    }
    return render(request, 'Hod/add_student.html', context=diction)


@login_required
def View_student(request):
    student_data = Student.objects.all()
    diction = {
        'student_data':student_data
    }
    return render(request, 'Hod/view_student.html', context=diction)



@login_required
def Edit_student(request, id):
    student_data = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Sessin_year.objects.all()

    diction = {
        'student_data':student_data,
        'course':course,
        'session_year':session_year,
    }
    return render(request, 'Hod/edit_student.html', context=diction)

def Updte_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')
        address = request.POST.get('address')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if profile_pic !=None and profile_pic != '':
            user.profile_pic = profile_pic

        if password !=None and password != '':
            user.set_password(password)
        
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.ciurse_id = course

        session_year = Sessin_year.objects.get(id=session_id)
        student.session_year_id = session_year
        student.save()
        messages.success(request, 'Student info update successfully!')
        return redirect('view_student')

    diction = {}
    return render(request, 'Hod/edit_student.html', context=diction)

@login_required
def Delete_student(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Student Successfully deleted!')
    return redirect('view_student')


@login_required
def Add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')

        course = Course(
            course_name=course_name
        )
        course.save()
        messages.success(request, 'Course are successfully added!')
        return redirect('add_course')
    
    diction = {}
    return render(request, 'Hod/add_cource.html')

@login_required
def View_course(request):
    course_data = Course.objects.all()
    diction = {
        'course_data':course_data
    }
    return render(request, 'Hod/view_course.html', context=diction)

def Edit_course(request, id):
    course_data = Course.objects.get(id=id)
    diction = {
        'course_data':course_data
    }
    return render(request, 'Hod/Edit_cource.html', context=diction)

@login_required
def Update_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        
        course = Course.objects.get(id=course_id)
        course.course_name = course_name
        course.save()
        messages.success(request, 'Course Successfully Updated!')
        return redirect('view_course')
        
    return render(request, 'Hod/view_course.html', context={})


@login_required
def Delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are successfully deleted!')
    return redirect('view_course')


@login_required
def Add_staff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already taken!')
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Already taken!')
            return redirect('add_staff')

        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                User_type = 2

            )

            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender
            )

            staff.save()
            messages.success(request, 'Sraff successfully added!')
            return redirect('add_staff')

        

    diction = {}
    return render(request, 'Hod/Add_staff.html', context=diction)



def View_staff(request):
    staff_data = Staff.objects.all()
    diction = {
        'staff_data':staff_data,
    }
    return render(request, 'Hod/view_staff.html', context=diction)
@login_required
def Edit_staff(request, id):
    staff_data = Staff.objects.filter(id=id)

    diction = {
        'staff_data':staff_data,
    }
    return render(request, 'Hod/edit_staff.html', context=diction)
@login_required
def Update_staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')


        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        
        if profile_pic !=None and profile_pic != '':
            user.profile_pic = profile_pic

        if password !=None and password != '':
            user.set_password(password)
        
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.address = address
        staff.gender = gender

        staff.save()
        messages.success(request, 'Staff Seccessfully Udated!')
        return redirect('view_staff')
    return render(request, 'Hod/edit_staff.html')

@login_required
def Delete_staff(request, id):
    staff = CustomUser.objects.get(id=id)
    staff.delete()
    return redirect('view_staff')


@login_required
def Add_subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            subject_name = subject_name,
            course = course,
            staff = staff,
        )

        subject.save()
        messages.success(request, 'Subject added Successfully!')
        return redirect('add_subject')

    diction ={
        'course':course,
        'staff':staff,
    }
    return render(request, 'Hod/add_subject.html', context=diction)


@login_required
def view_subject(request):
    subject_data = Subject.objects.all()
    diction = {
        'subject_data':subject_data
    }
    return render(request, 'Hod/view_subject.html', context=diction)


@login_required
def Edit_subject(request, id):
    subject_data = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    diction = {
        'subject_data':subject_data,
        'course':course,
        'staff':staff,
    }
    return render(request, 'Hod/edit_subject.html', context=diction)

@login_required
def Update_subject(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        subject_id = request.POST.get('subject_id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        

        subject = Subject.objects.get(id=subject_id)

        subject.subject_name = subject_name
        course = Course.objects.get(id=course_id)
        subject.course = course
        staff = Staff.objects.get(id=staff_id)
        subject.staff = staff

        subject.save()
        messages.success(request, 'Subject Successfully Updated!')
        return redirect('view_subject')

    diction = {}
    return render(request, 'Hod/edit_subject.html', context=diction)


@login_required
def Delete_Subject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.success(request, 'Subject Successfully Deleted!')
    return redirect ('view_subject')


@login_required
def Add_session(request):
    if request.method == 'POST':
        sesssion_start = request.POST.get('sesssion_start')
        session_end = request.POST.get('session_end')

        session = Sessin_year(
            session_start=sesssion_start,
            session_end=session_end
        )
        session.save()
        messages.success(request, 'Session year successfully added!')
        return redirect('add_session')
    context = {}
    return render(request, 'Hod/add_session.html', context)

@login_required
def View_session(request):
    session_data = Sessin_year.objects.all()
    context = {
        'session_data':session_data
    }
    return render(request, 'Hod/view_session.html', context)
@login_required
def Edit_session(request, id):
    session = Sessin_year.objects.filter(id=id)
    context = {
        'session':session
    }
    return render(request, 'Hod/Edit_session.html', context)

@login_required
def Update_session(request):
    if request.method=='POST':
        sesssion_start = request.POST.get('sesssion_start')
        sesssion_id = request.POST.get('sesssion_id')
        session_end = request.POST.get('session_end')

        session = Sessin_year.objects.get(id=sesssion_id)
        session.session_start = sesssion_start
        session.session_end = session_end
        session.save()
        messages.success(request, 'Session Information successfully updated!')
        return redirect('view_session')


    return render(request, 'Hod/Edit_session.html')

@login_required
def Delete_session(request, id):
    session = Sessin_year.objects.filter(id=id)
    session.delete()
    return redirect('view_session')

@login_required
def staff_send_notification(request):
    staff_data = Staff.objects.all()
    see_notificatio = Staff_Notification.objects.all().order_by('-id')
    context = {
        'staff_data':staff_data,
        'see_notificatio':see_notificatio
    }
    return render(request, 'Hod/send_staff_notification.html', context)


@login_required
def Save_staff_notification(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staaff_if')
        massege = request.POST.get('massege')

        staff = Staff.objects.get(admin=staff_id)

        notification =Staff_Notification(
            staff_id = staff,
            messege = massege
        )
        notification.save()
        messages.success(request, 'Notification are successfully sent!')
        return redirect('send_notification')
@login_required
def Staff_leave_view(request):
    staff_leave = Staff_leav.objects.all()

    context = {
        'staff_leave':staff_leave
    }
    return render(request, 'Hod/staff_leave.html', context)
@login_required
def Apply_approve(request, id):
    staff_leave = Staff_leav.objects.get(id=id)
    staff_leave.status = 1
    staff_leave.save()
    return redirect('staff_leave_view')

@login_required
def Apply_Disapprove(request, id):
    staff_leave = Staff_leav.objects.get(id=id)
    staff_leave.status = 2
    staff_leave.save()
    return redirect('staff_leave_view')


def staff_feedback_hod(request):
    staff_feedback = Staff_feedback.objects.all()

    context = {
        "staff_feedback":staff_feedback
    }
    return render(request, 'Hod/staff_feedback.html', context)


def staff_feedback_reply(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback_reply_save = Staff_feedback.objects.get(id=feedback_id)
        feedback_reply_save.reply_feedback = feedback_reply
        feedback_reply_save.save()
        return redirect('staff_feedback_hod')

def Student_send_notification(request):
    student = Student.objects.all()
    studnet_notification = Student_Notification.objects.all().order_by('-id')

    context = {
        'student':student,
        'studnet_notification':studnet_notification
    }
    return render(request, 'Hod/student_notification.html', context)

def Save_student_notification(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        massege = request.POST.get('massege')

        student = Student.objects.get(admin=student_id)

        student_notification = Student_Notification(
            student_id = student,
            messege=massege
        )
        student_notification.save()
        return redirect('send_student_notification')

def Student_feedback_hod(request):
    stu_feedback = Student_feedback.objects.all()
    context = {
         'stu_feedback':stu_feedback
    }
    return render(request, 'Hod/student_feedback.html', context)


def student_feedback_reply(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        student_feedback_reply = Student_feedback.objects.get(id=feedback_id)

        student_feedback_reply.reply_feedback = feedback_reply
        messages.success(request, 'Reply successfully send!')
        student_feedback_reply.save()
        return redirect('hod_student_feedback')


def Student_leave_view(request):
    student_leave_data = Student_leav.objects.all()
    context = {
        'student_leave_data':student_leave_data
    }
    return render(request, 'Hod/student_leave.html',context )


def student_approve_leave(request, stutas):
    student_leave = Student_leav.objects.get(id=stutas)
    student_leave.status = 1
    student_leave.save()
    return redirect('student_leave_view')

def student_disapprove_leave(request, stutas):
    student_leave = Student_leav.objects.get(id=stutas)
    student_leave.status = 2
    student_leave.save()
    return redirect('student_leave_view')

def View_attendance(request):
    subject = Subject.objects.all()
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
    return render(request, 'Hod/view_attendance.html', context)