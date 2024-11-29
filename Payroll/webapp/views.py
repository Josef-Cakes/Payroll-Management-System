from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Admin, Salary, Deduction
from .forms import LoginForm

# Home view
def home(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('hr_dashboard')
            else:
                return redirect('home') 
    else:
        form = LoginForm()

    return render(request, 'index.html', {'form' : form})
        


# Admin (HR) dashboard view
def hr_dashboard_view(request):
    return render(request, 'human_resource/hr_dash.html', {})

# Employee dashboard view
def emp_dashboard_view(request):
    return render(request, 'employee/emp_dash.html', {})

# Salary dashboard view
def salary_report_view(request):
    # Retrieve all employees with their salaries and deductions
    employees_data = []

    for employee in Employee.objects.all():
        # Get the salary record for the employee's job
        salary_record = Salary.objects.filter(job=employee.job).first()
        deductions = Deduction.objects.filter(emp=employee)

        # Calculate total deductions
        total_deductions = sum(ded.ded_amount for ded in deductions)

        # Calculate the net salary
        net_salary = (salary_record.amount - total_deductions) if salary_record else 0

        # Append the data to the list
        employees_data.append({
            'employee': employee,
            'base_salary': salary_record.amount if salary_record else 0,
            'total_deductions': total_deductions,
            'net_salary': net_salary,
        })

    return render(request, 'salary_report.html', {'employees_data': employees_data})

# Leave dashboard view
def leave_dashboard_view(request):
    return render(request, 'leave_report.html')

def log_out_view(request):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    return render(request, 'home.html', {})
