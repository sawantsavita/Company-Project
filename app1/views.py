from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from app1.models import Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        cid = request.POST.get("company_id")
        name = request.POST.get('company_name')
        address = request.POST.get('company_address')
        no_of_employees = request.POST.get('company_no_of_employees')
        est_date = request.POST.get('company_est_date')
        is_govt_registered = request.POST.get('company_is_govt_registered')
        if is_govt_registered == 'Yes':
            is_govt_registered = True
        else:
            is_govt_registered = False
        print(name, address, no_of_employees, est_date, is_govt_registered)
        if name and address and no_of_employees and est_date and is_govt_registered:
            if not cid:
                c1 = Company(name=name, address=address, no_of_employees=no_of_employees,
                             est_date=est_date, is_govt_registered=is_govt_registered)
                c1.save()
            else:
                obj = Company.objects.get(id=cid)
                obj.name = name
                obj.address = address
                obj.no_of_employees = no_of_employees
                obj.est_date = est_date
                obj.is_govt_registered = is_govt_registered
                obj.save()
        else:
            print("Enter valid details of Company")
        return redirect('home')

@login_required
def show_company(request):
    # print(Company.objects.all())
    return render(request, "show_company.html", {"all_company": Company.objects.filter(is_active=True), "active": True})


@login_required
def show_inactive_company(request):
    return render(request, "show_company.html", {"all_company": Company.objects.filter(is_active=False), "active": False})


@login_required
def single_company(request, id):
    return render(request, "show_single_record.html", {"single_record": Company.objects.get(id=id)})


@login_required
def show_company_second_db(request):
    all_company = Company.objects.using("SECOND_DB").all()
    print(all_company)
    return render(request, 'show_company.html', {"all_company": Company.objects.using("SECOND_DB").filter(is_active=True), "active": True})


@login_required
def single_company_second_db(request, id):
    return render(request, "show_single_record.html", {"single_record": Company.objects.using("SECOND_DB").get(id=id)})


@login_required
def update(request, id):
    obj = Company.objects.get(id=id)
    print(obj)
    return render(request, "home.html", {"single_record": Company.objects.get(id=id)})


@login_required
def hard_delete(request, id):
    obj = Company.objects.get(id=id)
    obj.delete()
    return redirect('home')


@login_required
def soft_delete(request, id):
    obj = Company.objects.get(id=id)
    obj.is_active = False
    obj.save()
    return redirect("show_company")


@login_required
def restore(request, id):
    obj = Company.objects.get(id=id)
    obj.is_active = True
    obj.save()
    return redirect("show_company")

# def register(request):
#     return render(request, "register.html", {"form": UserCreationForm})

import requests
GET_ALL_STUDENTS = "http://127.0.0.1:8000/api/get-all-student/"

def get_all_students(request):
    response = requests.request("GET", GET_ALL_STUDENTS)
    python_dict = response.json()
    return render(request, "student_data.html", {"data": python_dict})

# import requests
# # GET_SINGLE_STUD_URL = "http://127.0.0.1:8000/api/get-student/{}/"
# GET_ALL_STUDS = "http://127.0.0.1:8000/api/get-all-students/"
# # CREATE_STUD = "http://127.0.0.1:8000/api/create-student/"


# def get_all_student(request):
#     # response = requests.get(GET_ALL_STUDS)
#     response = requests.request("GET", GET_ALL_STUDS)
#     python_dict = response.json()  # json to python dict
#     return render(request, "student_data.html", {"data": python_dict})


