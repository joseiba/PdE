from django.shortcuts import render

# Create your views here.
def list_careers(request):
    return render(request, "career/list_careers.html")