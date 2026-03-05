from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
# Create your views here.
def about(request):
    return render(request,"about.html")
def form(request):
    return render(request, 'form.html')
def contact(request):
    return HttpResponse("<h1>ติดต่อเรา</h1>")