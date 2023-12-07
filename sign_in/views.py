from django.shortcuts import render 
  
# Create your views here. 
def Sign_In_View(request): 
    return render(request, "sign_in/sign_in.html")

def Sign_Out_View(request): 
    return render(request, "sign_in/sign_out.html")