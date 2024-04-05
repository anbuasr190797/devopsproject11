from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from scmapp.models import User, Admin, Book_ground
import datetime

# Create your views here.

#User Registration / Login Page
def index(request):
    return render(request,'registration.html')

#User Home Page
def user_home(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}

        if 'book_status' in request.session:
            data['status'] = request.session['book_status']

        return render(request,'user_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#User Ground Booking Page
def ground_booking(request):
    if 'uname' in request.session:
        data = {'date':datetime.date.today()}
        return render(request,'ground_booking.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#User Logout
def user_logout(request):
    if 'uname' in request.session:
        del request.session['uname']

    if 'book_status' in request.session:
        del request.session['book_status']

    return render(request,'registration.html')

#Admin Login Page
def admin_login(request):
    return render(request,'admin_login.html')

def admin_logout(request):
    if 'aname' in request.session:
        del request.session['aname']
 
    if 'event_status' in request.session:
        del request.session['event_status']
 
    return render(request,'admin_login.html')

#Admin Home Page
def admin_home(request):
    if 'aname' in request.session:
        data = {'name':request.session.get('aname')}
        return render(request,'admin_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#Admin View Bookings
def admin_booking(request):
    if 'aname' in request.session:
        booking = Book_ground.objects.all()
        data = {'booking':booking}
        return render(request,'admin_booking.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)

#BACKEND -> For User Registration
def test(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            user = User(name=name,email=email,gender=gender,password=password)
            user.save()
            request.session['uname'] = name
            return user_home(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For User Login
def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)

            if user.password == password:
                request.session['uname'] = name
                return user_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'registration.html',context=data)

        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For Admin Login
def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(name=name)

            if user.password == password:
                request.session['aname'] = name
                # return HttpResponse('ffaf')
                return admin_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'admin_login.html',context=data)

        except Exception as e:
            data = {'status':"Invalid Username"}
            return render(request,'admin_login.html',context=data)
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")

#BACKEND -> For Ground Booking
def db_ground_booking(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        time = request.POST.get('time')

        try:
            book = Book_ground.objects.get(date=date)
            data = {'status':'Please select other date'}
            return render(request,'ground_booking.html',context=data)
        except Exception as e:
            user = User.objects.get(name=request.session['uname'])
            book = Book_ground(uid=user.uid,name=user.name,mobile=mobile,date=date,time=time)
            book.save()
            request.session['book_status'] = "Booking successful"
            return user_home(request)
    else:
        return HttpResponse("Something went wrong!!!!!")
