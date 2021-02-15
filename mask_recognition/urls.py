from django.contrib import admin
from django.urls import path, re_path
from web import views

urlpatterns = [
    path('account/warnings/', views.warnings),

    path('account/employees/edit/<int:emp_id>/update/', views.update_employee),
    path('account/employees/edit/<int:emp_id>/', views.edit_employee),
    path('account/employees/delete/<int:emp_id>/', views.delete_employee),
    path('account/employees/add/', views.add_employee),
    path('account/employees/', views.employees),

    path('account/areas/camera/<int:cam_id>/delete/', views.delete_camera),
    path('account/areas/camera/<int:cam_id>/update/', views.update_camera),
    path('account/areas/camera/<int:cam_id>/', views.edit_camera),
    path('account/areas/edit/<int:area_id>/update/', views.update_area),
    path('account/areas/edit/<int:area_id>/', views.edit_area),
    path('account/areas/delete/<int:area_id>/', views.delete_area),
    path('account/areas/add_area/', views.add_area),
    path('account/areas/add_camera/', views.add_camera),
    path('account/areas/', views.areas),
    
    path('account/schedules/edit/<int:sched_id>/update/', views.update_schedule),
    path('account/schedules/edit/<int:sched_id>/', views.edit_schedule),
    path('account/schedules/delete/<int:sched_id>/', views.delete_schedule),
    path('account/schedules/add/', views.add_schedule),
    path('account/schedules/', views.schedules),

    path('account/backups/', views.backups),
    path('account/run_mask/', views.mask_detecting),
    path('account/backups/delete/<backup_name>/', views.delete_backup),
    path('account/backups/import/<backup_name>/', views._import),
    path('account/backups/export/', views.export),

    path('account/', views.account),

    path('admin/<int:account_id>/employees/<int:employee_id>/', views.admin_employee),
    path('admin/<int:account_id>/', views.detailed_account),

    path('admin/edit/<int:account_id>/update_account/', views.update_account),
    path('admin/edit/<int:account_id>/', views.edit_account),
    path('admin/delete/<int:account_id>/', views.delete_account),
    path('admin/', views.admin),

    path('contacts/', views.contacts),
    path('register/', views.register),
    
    re_path(r'.*ukr/', views.ukr),
    re_path(r'.*eng/', views.eng),

    re_path(r'.*contacts_redirect/', views.contacts_redirect),
    re_path(r'.*backups_redirect/', views.backups_redirect),
    re_path(r'.*registration/', views.registration),
    re_path(r'.*signout/', views.signout),
    path('signin/', views.signin),
    path('', views.index),
]
