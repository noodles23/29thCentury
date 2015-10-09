from django.shortcuts import render


# Create your views here.
def demo_dash(request):
    if request.user.is_authenticated():
	    return render(request, "demo_dash.html", {})
    else:
	   return render(request, "home.html", {})