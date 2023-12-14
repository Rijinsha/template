from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    #check pswrd usrnm is eul
    if request.method =='POST':
        uname=request.POST['username']
        pswrd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswrd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username= request.POST['usrname']
        fname = request.POST['firstname']#here firstname is the name of register.html
        lname=request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['password1']
        #here red is the bd name and uname is the variable name(email=email)
        #check password cpswrd is equl
        if password==cpassword:
            #check user name is alredy create in db
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken") #messages mean display in web page error msg
                return redirect('register')  #refresh register page
            elif User.objects.filter(email=email).exists():   #else check email allso
                messages.info(request,"email Taken")
                return redirect('register')
            else:# abou 3 condetions are true then data save in db
               user= User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
               user.save();
               return redirect('login')
            print ("user created")
        #    messages.info(request,"user create")
        else:
            #print("password not maching")
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/') # resgtrn is sucses go home page
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')