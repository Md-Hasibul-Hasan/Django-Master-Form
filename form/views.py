from django.shortcuts import render, redirect
from .forms import Profile_Form
from .models import Profile_Model, JobCity

# Create your views here.

def home(request):
    # JobCity.populate_job_cities()  # Ensure cities exist
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










# ক্লিন ডাটা নিয়ে ফর্ম 

# from django.shortcuts import render, redirect
# from .forms import Profile_Form
# from .models import Profile_Model

# # Create your views here.

# def form(request):
#     info = Profile_Model.objects.all()
#     if request.method == 'POST':
#         form = Profile_Form(request.POST, request.FILES)
#         if form.is_valid():
#             name=form.cleaned_data.get('name')
#             dob=form.cleaned_data.get('dob')
#             gender=form.cleaned_data.get('gender')
#             locality=form.cleaned_data.get('locality')
#             city=form.cleaned_data.get('city')
#             pin=form.cleaned_data.get('pin')
#             state=form.cleaned_data.get('state')
#             mobile=form.cleaned_data.get('mobile')
#             email=form.cleaned_data.get('email')
#             job_city=form.cleaned_data.get('job_city')
#             password=form.cleaned_data.get('password')
#             profile_image=form.cleaned_data.get('profile_image')
#             my_file=form.cleaned_data.get('my_file')

#             s=Profile_Model(name=name,dob=dob,gender=gender,locality=locality,city=city,pin=pin,state=state,mobile=mobile,email=email,password=password,job_city=job_city,profile_image=profile_image,my_file=my_file)
#             s.save()
#             return redirect('form')
#     else:
#         form = Profile_Form()
#     return render(request, 'django_form/home.html', {'form': form, 'info': info})

# def info(request, id):
#     info = Profile_Model.objects.get(pk=id)
#     return render(request, 'django_form/info.html', {'info': info})