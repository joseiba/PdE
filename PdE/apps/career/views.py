from django.shortcuts import redirect, render
from django.contrib import messages

from apps.career.form import CareerForm
from apps.career.models import Career

# Create your views here.
def list_careers(request):
    careers = Career.objects.all().order_by('-last_modified')
    count = careers.count
    context = {'careers' : careers, 'count': count}
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