from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.
def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        cpassword = req.POST['password1']
        
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"Email Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email )
                user.save();
                return redirect('login')
        else:
            messages.info(req,"Password Not Matching")
            return redirect('register')
           
    return render(req, "reg.html")

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/')  
        else:
            messages.info(req, "Invalid username or password")
            return redirect('login')
        
    return render(req, "login.html")

def logout(req):
    auth.logout(req)
    return redirect('/')