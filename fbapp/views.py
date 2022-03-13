from django.shortcuts import render

from .forms import EnForm
from .models import EnModel

def user_fb(request):
	if request.method == "POST":
		na=request.POST.get("name")
		em=request.POST.get("email")
		ms=request.POST.get("enq_msg")
		data=EnModel(name=na,email=em,enq_msg=ms)
		data.save()
		fm=EnForm()
		return render(request,"user_fb.html",{"fm":fm,"msg":"We will get back to you"})
	else:
		fm=EnForm()
		return render(request,"user_fb.html",{"fm":fm})
