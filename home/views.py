from django.shortcuts import render

# Create your views here.

def home_display(request):
	context={
			"title": "Home",
		}
	return render(request,"home/home.html",context)

def about_page(request):
	contex = {
		"title": "About"
	}
	return render(request,'about.html',contex)