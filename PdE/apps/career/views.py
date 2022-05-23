from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator


from apps.career.form import CareerForm
from apps.career.models import Career

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
    return render(request, "semester/list_semesters_career.html",)    