from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm
import cv2
from .models import Images




def img_upload(request):
    return render(request, 'music/img_upload.html', {'apna_var' : 'a',})

def enter_tag(request):
    if request.method == "POST":
        tagg = request.POST['tagg'] #or pass values in enter tag
        username = request.POST['username']
        selected_image = request.POST['selected_image']
        result=get_object_or_404(Images, username=username)
       
        if selected_image == "pass_img" and tagg == result.tagg:
            
            return render(request, 'music/success.html', { 'tagg' : tagg, 'username' : username , 'user' : user})
        else:
            return render(request, 'music/not_valid.html')
    else:
        return render(request, 'music/login.html')#return render(request, 'music/enter_tag.html', {'selected_image' : '/media/4.jpg',})


def img_select(request):
    if request.method == "POST":
        username = request.POST['username'] #or pass values in enter tag
        #usernamee = "me"
        option= request.POST['img1']
        result=get_object_or_404(Images, username=username)
        return render(request, 'music/enter_tag.html', {'image' : result, 'option' : option })
    else:
    	return render(request, 'music/login.html')

def index(request):
    return render(request, 'music/index.html')
    


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        #get pk where username=username
        result=get_object_or_404(Images, username=username)
        #result=Images.objects.get(username=username)
        if result:
            #return render(request, 'music/login1.html', {'error_message': result.tagg})
            return render(request, 'music/img_select.html', {'image' : result})
        else:
            return render(request, 'music/login.html', {'error_message': 'username is not correct'})
    
    return render(request, 'music/login.html', {'apni_img1' : '/media/1.jpg', 
        })


def success_page(request):
   
    return render(request, 'music/success.html')

def not_valid(request):
   
    return render(request, 'music/not_valid.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                return render(request, 'music/success.html')
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)

