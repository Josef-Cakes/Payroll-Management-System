from django.db import models

class Job(models.Model):
    job_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    job_dept = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_ID = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    emp_email = models.EmailField(unique=True)
    emp_pass = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Admin(models.Model):
    admin_ID = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Salary(models.Model):
    salary_ID = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Salary ID: {self.salary_ID}"


class Deduction(models.Model):
    ded_ID = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ded_type = models.CharField(max_length=255)
    ded_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Deduction ID: {self.ded_ID}"


class Leave(models.Model):
    leave_ID = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)
    reason = models.TextField()

    def __str__(self):
        return f"Leave ID: {self.leave_ID}"


class Payroll(models.Model):
    payroll_ID = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    report = models.TextField()
    ded = models.ForeignKey(Deduction, on_delete=models.CASCADE, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payroll ID: {self.payroll_ID}"
