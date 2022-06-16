from django.shortcuts import render

# Create your views here.
def handler_404(request, exception):
    return render(request, "handler/handler_404.html", status=404)

def handler_500(request, *args, **argv):
    return render(request, "handler/handler_500.html", status=500)