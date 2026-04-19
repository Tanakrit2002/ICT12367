from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person
from django.db.models import Q

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

def edit(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save() 
        return redirect("/")       
    return render(request, 'edit.html', {'person': person})

# Create your views here.
def index(request):
    # 1. ดึงข้อมูลประชากรทั้งหมดมาก่อน (กรณีที่ยังไม่ได้ค้นหา)
    all_Person = Person.objects.all()
    
    # 2. รับค่าคำค้นหาจากช่องค้นหา (name="q")
    query = request.GET.get('q')
    
    # 3. ตรวจสอบว่ามีคำค้นหาถูกพิมพ์ส่งมาหรือไม่
    if query:
        # ถ้ามีคำค้นหา ให้นำ all_Person มากรองข้อมูลเฉพาะคนที่ชื่อตรงกับค่าค้นหา
        all_Person = all_Person.filter(name__icontains=query)
        
    # 4. ส่งข้อมูลไปแสดงผลที่ template (ถ้าไม่มี query ก็จะแสดงทั้งหมดตามข้อ 1)
    return render(request, "index.html", {"all_person": all_Person})