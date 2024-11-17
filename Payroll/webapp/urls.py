from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=' '),                     # Home page
    path('log_in/', views.login_view, name='login'),       # Login page
    path('hr_dash/', views.hr_dashboard_view, name='hr_dashboard'),  # HR dashboard
    path('emp_dash/', views.emp_dashboard_view, name='emp_dashboard'),  # Employee dashboard
    path('salary_dash/', views.salary_report_view, name='salary_report'),  # Salary report view
    path('leave_dash/', views.leave_dashboard_view, name='leave_report'),  # Leave report 
    path('logout/', views.log_out_view, name="logout"),
]