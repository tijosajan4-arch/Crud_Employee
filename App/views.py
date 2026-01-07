from django.shortcuts import render,redirect
from App import models

# Create your views here.

def employee_list(request):
    employees = models.Employee.objects.all()
    return render(request, 'App/employee_list.html',{'employees':employees})

def add_employee(request):
    if request.method == 'POST':
        add_name = request.POST.get('value_name')
        add_age = request.POST.get('value_age')
        add_place = request.POST.get('value_place')
        add_job = request.POST.get('value_job')
        add_salary = request.POST.get('value_salary')
        add_contact = request.POST.get('value_contact')
        add_email = request.POST.get('value_email')

        employee = models.Employee(name = add_name,age = add_age,place = add_place,job= add_job,salary = add_salary,contact= add_contact,email = add_email)
        employee.save()

        return redirect('employee')
    return render(request,'App/add_employee.html')

def edit_employee(request,emp_id):
    employee = models.Employee.objects.get(id=emp_id)
    if request.method == 'POST':
        employee.name = request.POST.get('edit_name')
        employee.age = request.POST.get('edit_age')
        employee.place = request.POST.get('edit_place')
        employee.job = request.POST.get('edit_job')
        employee.salary = request.POST.get('edit_salary')
        employee.contact = request.POST.get('edit_contact')
        employee.email = request.POST.get('edit_email')

        employee.save()
        return redirect('employee')

    return render(request,'App/edit_employee.html',{'employee':employee})

