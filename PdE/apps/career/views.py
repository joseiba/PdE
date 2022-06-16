from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from apps.career.form import CareerForm, SemesterForm
from apps.career.models import Career, Semester

# Create your views here.
def list_careers(request):
    careers = Career.objects.all().order_by('-last_modified')
    paginator = Paginator(careers, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = careers.count
    context = {'page_obj' : page_obj,  'count': count}
    return render(request, "career/list_careers.html", context)


def add_careers(request):
    form = CareerForm
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha agregado correctamente!')
            return redirect('/career/list')
    context = {'form': form}
    return render(request, "career/add_careers.html", context)

def edit_careers(request, id):
    career = Career.objects.get(id=id)
    form = CareerForm(instance=career)
    if request.method == 'POST':
        form = CareerForm(request.POST, instance=career)
        if not form.has_changed():
            return redirect('/career/edit/' + str(id))
        if form.is_valid():
            career = form.save(commit=False)
            career.save()
            return redirect('/career/list')
    context = {'form': form, 'career': career}
    return render(request, 'career/edit_careers.html', context)

def list_semester_career(request, id):
    semester = Semester.objects.filter(Q(id_career__id__icontains=id)).order_by('-last_modified')
    paginator = Paginator(semester, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = semester.count
    context = {'page_obj' : page_obj,  'count': count, 'id':id}   
    return render(request, "semester/list_semesters_career.html", context)

def add_semester_career(request, id):
    form = SemesterForm
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha agregado correctamente!')
            return redirect('/career=' + str(id)+ '/semester/list')
    context = {'form': form, 'id': id}
    return render(request, "semester/add_semester.html", context)

def edit_semester_career(request, id):
    semester = Semester.objects.get(id=id)
    form = SemesterForm(instance=semester)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if not form.has_changed():
            return redirect('/career=' + str(semester.id_career.id)+ '/semester/list')
        if form.is_valid():
            career = form.save(commit=False)
            career.save()
            return redirect('/career=' + str(semester.id_career.id)+ '/semester/list')
    context = {'form': form, 'semester': semester}
    return render(request, 'semester/edit_semester.html', context)   