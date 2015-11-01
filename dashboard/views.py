from django.shortcuts import render

# Create your views here.
def demo_home(request):
    # if request.user.is_authenticated():
	    return render(request, "demo_home.html", {})
    # else:
	   #return render(request, "registration/login.html", {})
	   
	   
def zzz(request):
    # if request.user.is_authenticated():
	    return render(request, "zzz.html", {})