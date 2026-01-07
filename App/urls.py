from django.urls import path
from App import views

urlpatterns = [
    path('',views.employee_list,name='employee'),
    path('add/',views.add_employee,name='add_employee'),
    path('edit/<int:emp_id>/',views.edit_employee,name='edit_employee'),
    path('delete/<int:emp_id>/',views.delete_employee,name='delete_employee'),
]
