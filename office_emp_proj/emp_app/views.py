from django.shortcuts import render, HttpResponse
from . models import Employee, Department, Role
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q



# Create your views here.
def index(request):
    return render(request , 'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request , 'view_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        second_name = request.POST.get('second_name', '')
        dept = int(request.POST.get('dept', 0))
        salary = int(request.POST.get('salary', 0))
        bonus = int(request.POST.get('bonus', 0))
        role = int(request.POST.get('role', 0))
        Phone = int(request.POST.get('Phone', 0))
        new_employee = Employee(first_name= first_name, second_name=second_name, dept_id= dept, salary= salary, bonus=bonus, role_id = role, Phone= Phone, hire_date= datetime.now())
        new_employee.save()
        return HttpResponse('Succesfully added new employee')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:    
        return HttpResponse('An exception has occured!')




def rem_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed= Employee.objects.get(id= emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Emplyoee removed successfully')
        except:
            return HttpResponse('Enter a valid ID')
    emps = Employee.objects.all()
    context ={
        'emps': emps
    }
    return render(request , 'rem_emp.html', context)

"""def filt_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps= emps.filter(Q(first_name__icontains = name)| Q(second_name__icontains = name))
        if dept:
            emps= emps.filter(dept_name__icontains = dept)
        if role:
            emps = emps.filter(role_name__icontains = role)
        context ={
           'emps': emps
       }
        return render(request , 'view_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filt_emp.html')
    
    else:
        return HttpResponse('An error has occured')"""
def filt_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(second_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__role__icontains=role)
        
        context = {'emps': emps}
        return render(request, 'view_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filt_emp.html')
    
    else:
        return HttpResponse('An error has occurred')
  