from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('assignrole/', views.assign_role, name='assign_role'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admission/', views.admission, name='admission'),
    path('admissionlist/', views.admissionlist, name='admissionlist'),

    path('studentdetails/<int:pk>/', views.studentdetails, name='studentdetails'),
    path('update-student/<int:pk>/',views.update_student_information, name='update_student_information'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),

    path('approve_student/<int:pk>/', views.approve_student, name='approve_student'),
    path('students/approvedlist/', views.approvedlist, name='approvedlist'),
    path('student/approvedlist-addunits/', views.approvedlist_addunits, name='approvedlist_addunits'),

    path('approve_student/details/<int:pk>/', views.approved_student_details, name='approved_student_details'),
    path('units/register-units/<int:pk>/', views.register_units, name='register_units'),
    path('units/view-units/<int:pk>/', views.view_units, name='view_units'),
    path('ict/ictstudents/', views.ict_list, name='ictstudents'),
    path('business/business_students/', views.bcom_list, name='business_students'),
    path('social-sciences/shs/', views.bcom_list, name='shs'),
    path('units/view-myunits/', views.view_myunits, name='view_myunits'),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
