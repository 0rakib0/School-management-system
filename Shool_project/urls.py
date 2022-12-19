from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views, stu_views, staff_views, hod_views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    # -----------------> Login&logout Path <------------------
    path('', views.loadin_page, name='login'),
    path('doLogin/', views.do_login, name='dologin'),
    path('dologout/', views.doLogout, name='doLogout'),

    # -----------------> profile path <-----------------------
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.Profile_update, name='profile_update'),

    # ----------------> HOD paths <---------------------
    path('Hod/home/', hod_views.hod , name='hod_home'),
    path('hod/add/student/', hod_views.add_student, name='add_student'),
    path('hod/student/view/', hod_views.View_student, name='view_student'),
    path('hod/edit/student/<str:id>/', hod_views.Edit_student, name='edit_student'),
    path('hod/update/student/',hod_views.Updte_student, name='update_student'),
    path('hod/delete/student/<str:admin>/', hod_views.Delete_student, name='delete_student'),

    path('hod/add/staff', hod_views.Add_staff, name='add_staff'),
    path('hod/view/staff/', hod_views.View_staff, name='view_staff'),
    path('hod/edit/staff/<str:id>/', hod_views.Edit_staff, name='edit_staff'),
    path('hod/update/staff/', hod_views.Update_staff, name='update_staff'),
    path('hod/delete/staff/<str:id>/', hod_views.Delete_staff, name='delete_staff'),


    path('hod/add/subject/', hod_views.Add_subject, name='add_subject'),
    path('hod/view/subject', hod_views.view_subject, name='view_subject'),
    path('hod/edit/subject/<str:id>/', hod_views.Edit_subject, name='edit_subject'),
    path('hod/update/subject/', hod_views.Update_subject, name='update_subject'),
    path('hod/delete/subject/<str:id>/', hod_views.Delete_Subject, name='delete_subject'),

    path('hod/course/add/', hod_views.Add_course, name='add_course'),
    path('hod/view/course/', hod_views.View_course, name='view_course'),
    path('hod/edit/course/<str:id>/', hod_views.Edit_course, name='edit_course'),
    path('hod/update/course/', hod_views.Update_course, name='updated_course'),
    path('hod/delete/course/<str:id>/', hod_views.Delete_course, name='delete_course'),

    path('hod/session/add/', hod_views.Add_session, name='add_session' ),
    path('hod/view/session/', hod_views.View_session, name='view_session'),
    path('hod/edit/session/<str:id>/', hod_views.Edit_session, name='edit_session'),
    path('hod/update/session/', hod_views.Update_session, name='update_session'),
    path('hod/delete/session/<str:id>/', hod_views.Delete_session, name='delete_session'),
    path('staff/leave-view/', hod_views.Staff_leave_view, name='staff_leave_view'),
    path('staff/leave/aprove/<str:id>/', hod_views.Apply_approve, name='staff_leave_approve'),
    path('staff/leave/disaprove/<str:id>/', hod_views.Apply_Disapprove, name='staff_leave_disapprove'),
    path('staff/feedback/', hod_views.staff_feedback_hod, name='staff_feedback_hod'),
    path('staff/fedback/reply', hod_views.staff_feedback_reply, name='staff_feedback_reply'),
    path('student/send/notification', hod_views.Student_send_notification, name='send_student_notification'),
    path('save/student/notification', hod_views.Save_student_notification, name='save_student_notification' ),
    path('student/feedback-hod/', hod_views.Student_feedback_hod, name='hod_student_feedback'),
    path('student/feedback/replay', hod_views.student_feedback_reply, name='student_feedback_reply'),
    path("student/leave/view", hod_views.Student_leave_view, name="student_leave_view"),
    path('student/approve/leave/<str:stutas>/', hod_views.student_approve_leave, name='studenr_leave_approve'),
    path('student/disapprove/leave/<str:stutas>/', hod_views.student_disapprove_leave, name='studenr_leave_disapprove'),
    path('hod/view/attendance/', hod_views.View_attendance, name='hod_view_attendance'),



    # staff notificaytion url here
    path('hod/send/staff_notification', hod_views.staff_send_notification, name='send_notification'),
    path('hod/save/staff_notificstion/', hod_views.Save_staff_notification, name='save_staff_notification'),


    # ------------------------> Staff URL <---------------------------
    path('Staff/home/', staff_views.Staff_Home, name='staff_home'),
    path('staff/notificastion/', staff_views.Notification, name='notification'),
    path('mark/notification/<str:status>/', staff_views.Mark_notification, name='staff_mark_notification'),
    path('Staff/Apply-leav/', staff_views.Apply_leav, name='staff_apply_leav'),
    path('staff/apply_leave_save/', staff_views.Staff_Apply_leave_save, name='Staff_apply_leave_save'),
    path('Staff/Feedback/', staff_views.Staff_Feefback, name='staff_feedback'),
    path('staff/save-feedback/', staff_views.Staff_save_feedback, name='staff_save_feedback'),
    path('staff/take/attendance/', staff_views.Take_attendance, name='take_attendance'),
    path('save/student/attendance/', staff_views.Save_attendance, name='save_attendance' ),
    path('student/view/attendance/', staff_views.view_attendance, name='view_attendance'),
    path('staff/add/result/', staff_views.Add_result, name='add_result'),
    path('save/student/result/', staff_views.Save_student_rtesult, name='save_result'),


    #--------------------------> Student views <-------------------------

    path('student/home', stu_views.Student_home, name='stu_home'),
    path('studnet/notification/', stu_views.Notification, name='student_notification'),
    path('student/mark/nitification/<str:status>/', stu_views.mark_notification, name='student_mark_notification'),
    path('student/feedback/', stu_views.Student_feedback_show, name='student_feedback'),
    path('studfent/save/feedback', stu_views.Student_save_feedback, name='student_save_feedback'),
    path('studdent/leave/apply', stu_views.Student_leave_apply, name='student_leave'),
    path('student/leave/save/', stu_views.student_leave_save, name='student_leave_save'),
    path('student/vew/attendance/', stu_views.Student_view_attendance, name='student_view_attendance'),
    path('student/view/result/', stu_views.Student_view_result, name='student_view_result')

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)