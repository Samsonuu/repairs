from django.urls import path
from .views import login_view, logout_view, register, home, submit_report, report_success,complete_repair,view_reports

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('submit/', submit_report, name='submit_report'),
    path('success/', report_success, name='report_success'),
    path('complete/<int:repair_id>/', complete_repair, name='complete_repair'),
    path('view_reports/', view_reports, name='view_reports'),
]
