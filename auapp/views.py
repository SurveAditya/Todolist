from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from email_auth_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

def user_signup(request):
	if request.method == "POST":
		un=request.POST.get("un")
		try:
			usr=User.objects.get(username=un)
			return render(request,"user_signup.html",{"msg":"email already reg"})
		except User.DoesNotExist:
			pw = ""
			text="abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(5):
				pw=pw+text[randrange(len(text))]
			sub="My first email"
			msg="Your password is "+str(pw)
			sender=EMAIL_HOST_USER
			rvr=[str(un)]
			send_mail(sub,msg,sender,rvr)
			usr=User.objects.create_user(username=un,password=pw)
			usr.save()	
			return redirect("user_login")
	else:
		return render(request,"user_signup.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
	
		if usr is None:
			return render(request,"user_login.html",{"msg":"Invalid Login"})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"user_login.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")


def user_np(request):
	if request.method == "POST":
		un=request.POST.get("un")
		try:
			usr=User.objects.get(username=un)
			pw = ""
			text="abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(5):
				pw=pw+text[randrange(len(text))]
			sub="My first email"
			msg="Your password is "+str(pw)
			sender=EMAIL_HOST_USER
			rvr=[str(un)]
			send_mail(sub,msg,sender,rvr)
			usr.set_password(pw)
			usr.save()	
			return redirect("user_login")
		except:
			return render(request,"user_signup.html",{"msg":"Email is not registered"})
			
	else:
		return render(request,"user_np.html")
	
def user_cp(request):
	if request.method == "POST" and request.user.is_authenticated:
		un=request.user.username
		pw1=request.POST.get("pw1")
		pw2=request.POST.get("pw2")
		if pw1 == pw2:
			usr=User.objects.get(username=un)
			usr.set_password(pw1)
			usr.save()
			return redirect("user_login")
		else:
			return render(request,"user_signup.html",{"msg":"password did not match"})
	elif request.method == 'GET' and request.user.is_authenticated:
		return render(request,"user_cp.html")
	else:
		return redirect("user_login")	
				


