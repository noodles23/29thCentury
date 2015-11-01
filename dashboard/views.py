from django.shortcuts import render

# Create your views here.
def demo_home(request):
    # if request.user.is_authenticated():
	    return render(request, "demo_home.html", {})
    # else:
	   #return render(request, "registration/login.html", {})

def demo_sales(request):
    # if request.user.is_authenticated():
	    return render(request, "demo_sales.html", {})	 

def demo_customers(request):
    # if request.user.is_authenticated():
	    return render(request, "demo_customers.html", {})	 	    

def demo_acustomers(request):
    # if request.user.is_authenticated():
	    return render(request, "demo_acustomers.html", {})	 
	    
def demo_arefund(request):
    # if request.user.is_authenticated():
	    return render(request, "demo_arefund.html", {})	 
	    
def zzz(request):
    # if request.user.is_authenticated():
	    return render(request, "zzz.html", {})