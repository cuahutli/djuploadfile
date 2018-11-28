from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    ctx = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        ctx['url'] = fs.url(name)
    return render(request, 'upload.html', ctx)