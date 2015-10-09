from django.shortcuts import render

def about(request):
	    return render(request, "home.html", {})

def dash(request):
    if request.user.is_authenticated():
	    return render(request, "dash.html", {})
    else:
	   return render(request, "home.html", {})
