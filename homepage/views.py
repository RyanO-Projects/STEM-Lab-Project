from django.shortcuts import render
  
# Create your views here. 
def Homepage_View(request): 
    return render(request, "homepage/homepage.html")

