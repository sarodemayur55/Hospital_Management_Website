from django.shortcuts import render, HttpResponse, redirect
from .models import name, patient_appointment,  specialist, doctordata, Profile,contactus
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    Names = name.objects.all()
    # return HttpResponse("this is homepage")
    return render(request, 'index.html', {"Names":Names})

def about(request):
    return render(request, 'about.html')

def home(request):
    if request.user.is_authenticated:
        return redirect('patient')
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        Name=request.POST.get('name')
        # Gender=request.POST.get('gender')
        # print(Gender)
        # Mobile=request.POST.get('mobile')
        Email=request.POST.get('email')
        # Age=request.POST.get('age')
        Subject=request.POST.get('subject')
        Description=request.POST.get('description')
        Contactus=contactus(name=Name,email=Email,subject=Subject,description=Description)
        Contactus.save()
        messages.success(request, 'Thank You For Contacting Us')
        return redirect('home')
    return render(request, 'contact.html')

def covid(request):
    return render(request,'covid.html')

    # return HttpResponse("this is home")
def link(request):
    appointments=patient_appointment.objects.all()

    return render(request, 'link.html', {"appointments": appointments})
    # return HttpResponse("this is link")
def add(request):
    val1=int(request.POST['num1'])
    # val2=int(request.POST['num2'])
    # res=val1+val2
    # return render(request, "result.html", {"result":res})


def logout(request):
    auth.logout(request)
    return redirect('/')


def patient(request):
    if request.user.is_authenticated:
        p=Profile.objects.get(user_id = request.user.id)
        # passuser=User.objects.get(username=request.user.username)
        check = p.is_doctor
        if check==True:
            return redirect('doctor')
        else:
            f=request.user.get_full_name()
            return render(request,"patient.html",{"f":f})
        # return render(request,'patient.html')
    else:
        messages.info(request, "Login first!!!")
        return render(request, 'index.html')

def history(request):
    if request.user.is_authenticated:
        username=request.user.username
        h = patient_appointment.objects.filter(username=username)
        return render(request,"history.html",{"history":h})
    else:
        messages.info(request, "Login first!!!")
        return render(request, 'index.html')


def doctor(request):
    if request.user.is_authenticated:
        p=Profile.objects.get(user_id = request.user.id)
        check = p.is_doctor
        if check==True:
            f=request.user.get_full_name()
            p=patient_appointment.objects.filter(doctorusername=request.user.username)
            return render(request,'doctor.html',{"appointments":p,"f":f})
            render(request,"doctor.html")
        else:
            return redirect(patient)
        p=patient_appointment.objects.filter(doctorusername=request.user.username)
        return render(request,'doctor.html',{"appointments":p})
    else:
        messages.info(request, "Login first!!!")
        return render(request, 'index.html')
    

def login(request):
    if request.user.is_authenticated:
        return redirect('patient')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        s=User.objects.filter(username=username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("User logged in")
            # messages.info(request, "Logged In Successfullly")
            # return redirect('/')
            p=Profile.objects.get(user_id = request.user.id)
            check = p.is_doctor
            if check==True:
                return redirect('doctor')
            else:
                return redirect('patient')
            return redirect('patient')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
def appointment(request):
    if request.method == 'POST':
        Name=request.POST.get('name')
        Gender=request.POST.get('gender')
        print(Gender)
        Mobile=request.POST.get('mobile')
        Email=request.POST.get('email')
        Age=request.POST.get('age')
        Description=request.POST.get('description')
        Date = request.POST.get('date')
        username=request.user.username
        doctorname=request.POST.get('doctorname')
        print(doctorname)
        d=doctordata.objects.get(dname=doctorname)

        # p=patient_appointment.objects.get()
        Appointment=patient_appointment(name=Name,gender=Gender, mobile=Mobile, email=Email, age=Age, description=Description, date=Date,username=username,doctorname=doctorname,doctorusername=d.username)
        Appointment.save()
        messages.success(request, 'Appointment Scheduled Successfully')
        # return render(request, 'home.html')
        return redirect('patient')
    if request.user.is_authenticated:
        specialistmodel = specialist.objects.all()
        doctormodel = doctordata.objects.all()
        return render(request, 'appointment.html',{"specialistobj":specialistmodel,"doctorobj":doctormodel})
    
    # messages.info(request, "Login first!!!")
    return render(request, 'index.html')
    



def register(request):
    if request.user.is_authenticated:
        # messages.info(request, "You are already logged in!!!")
        return redirect('/')
    print("Page requested")
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists') 
                print('User taken')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                p=Profile(user=user, is_patient=True)
                p.save()

                # messages.info(request, 'User Created')
                print("User Created")
        else:
            print("password not matching")
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
