from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Admin, Salary, Deduction

# Home view
def home(request):
    return render(request, 'index.html')

# Login view
# Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # Check if the user is an Admin
        admin_user = Admin.objects.filter(admin_email=email).first()
        if admin_user and check_password(password, admin_user.admin_pass):
            request.session['user_id'] = admin_user.admin_ID  # Set admin ID
            request.session['user_role'] = 'admin'            # Set role to admin
            return redirect('webapp/hr_dashboard')                   # Redirect to HR dashboard

        # Check if the user is an Employee
        employee_user = Employee.objects.filter(emp_email=email).first()
        if employee_user and check_password(password, employee_user.emp_pass):
            request.session['user_id'] = employee_user.emp_ID  # Set employee ID
            request.session['user_role'] = 'employee'          # Set role to employee
            return redirect('webapp/emp_dashboard')                   # Redirect to Employee dashboard

        # If we reach here, the credentials are invalid
        messages.error(request, "Invalid email or password.")
    # If the request method is not POST, render the login page
    return render(request, 'webapp/index.html')


# Admin (HR) dashboard view
def hr_dashboard_view(request):
    if request.session.get('user_role') == 'admin':
        return render(request, 'hr_dash.html', {})
    return redirect('home')  # Redirect to home if not an admin

# Employee dashboard view
def emp_dashboard_view(request):
    if request.session.get('user_role') == 'employee':
        return render(request, 'emp_dash.html')
    return redirect('home')  # Redirect to home if not an employee

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
    logout(request)
    return redirect('home')
