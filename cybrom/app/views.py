from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.

# def landingpage(request):
#     return HttpResponse("<h1>The Dark World  </h1> <br/><h2>The Dark World  </h2> <br/><h3>The Dark World  </h3> <br/>")


# def home(request):
#     return HttpResponse("<h1>The Dark World  </h1> <br/><h2>The Dark World  </h2> <br/><h3>The Dark World  </h3> <br/>")



def home(request):
    return render(request,"home.html")
# def home(request):
#      return redirect("https://www.myntra.com/")