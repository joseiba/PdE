from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from apps.folder.models import Folder
from apps.folder.form import FolderForm
# Create your views here.
def list_folder_semester(request,id):
    folder = Folder.objects.filter(Q(id_semester__id__icontains=id)).order_by('-last_modified')
    paginator = Paginator(folder, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = folder.count
    context = {'page_obj' : page_obj,  'count': count, 'id':id}
    return render(request, "folder/list_folder.html", context)


def add_folder_semester(request, id):
    print(id)
    form = FolderForm
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha agregado correctamente!')
            return redirect('/career/semester=' + str(id)+ '/folder/list')
    context = {'form': form, 'id': id}
    print("llego aca "+ str(id))
    return render(request, "folder/add_folder.html", context)

