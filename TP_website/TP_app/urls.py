from django.contrib import admin
from django.urls import path
from . import views
app_name = 'TP_app'

urlpatterns = [
    path('', views.index, name= "index"),
    #Authentication
    path('register/', views.register_page, name= "register"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    path('TP_app/', views.register_student, name="register_student"),
    path('register_job/', views.register_job, name="register_job"),
    path('register_student_submit/', views.register_student_submit, name="register_student_submit"),
    path('register_job_submit/', views.register_job_submit, name="register_job_submit"),
    path('companies/', views.companies, name="companies"),
    path('upcoming_events/', views.upcoming_events, name="upcoming_events"),
    path('register_job_submit/', views.register_job_submit, name="register_job_submit"),
    path('add_company/', views.add_company, name="add_company"),
    path('add_company_submit/', views.add_company_submit, name="add_company_submit"),
    path('Statistics/', views.Statistics, name="Statistics"),
]
