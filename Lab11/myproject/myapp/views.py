from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request, 'index.html',{"all_person":all_Person})
# Create your views here.
def about(request):
    return render(request, 'about.html')

# def form(request):
    # return render(request, 'form.html')

def form(request) :
    if request.method == "POST" :
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = request.POST.get("age")
        # บันทึกลงฐานข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        # เปลี่ยนเส้นทางไปหน้าเเรก
        return redirect("/")
    else:

        # เเสดงฟอร์ม
        return render(request, 'form.html')