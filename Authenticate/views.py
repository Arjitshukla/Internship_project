from django.shortcuts import render,redirect
# from Authenticate.models import Post
from django.contrib import messages

# authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# login api authentication
def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")  # Error message
            return redirect('/user/login/')  # Redirect to login page on error

    return render(request, 'Authentication/login.html')

   
def  handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/user/signup/')

        if len(uname)<5:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/user/signup/')
        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Taken")
                return redirect('/user/signup/')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/user/signup/')
        except:
            pass
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup Success Please login!")
        return redirect('/user/login/')
    return render(request,'Authentication/signup.html')

def handlelogout(request):
   logout(request)
   messages.info(request,"Logout Success")
   return redirect('/')