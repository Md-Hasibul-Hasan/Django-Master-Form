from django.shortcuts import render, redirect
from .forms import Profile_Form
from .models import Profile_Model, JobCity

# Create your views here.

def home(request):
    info = Profile_Model.objects.all()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Profile_Form()
    return render(request, 'form/home.html', {'form': form, 'info': info})

def info(request, id):
    info = Profile_Model.objects.get(pk=id)
    return render(request, 'form/info.html', {'info': info})

def delete(request, id):
    info = Profile_Model.objects.get(pk=id)
    info.delete()
    return redirect('home')

def update(request, id):
    info = Profile_Model.objects.get(pk=id)

    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('info', id)
    else:
        form = Profile_Form(instance=info)

    return render(request, 'form/update.html', {'form': form, 'info': info})


