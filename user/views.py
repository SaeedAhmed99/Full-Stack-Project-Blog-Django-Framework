from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from user.forms import CreateUser, user_update, image_update
from django.contrib.auth.models import User
from user.forms import CreateUser, log_in_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def register(request):
    return render(request, 'user/register.html', {'title': 'التسجيل', 'form': CreateUser})


def register_back(request):
    try:
        user =User.objects.create_user( 
            request.POST['username'],
            request.POST['email'],
            request.POST['password']
        )
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        name = request.POST['username']
        fname = request.POST['first_name']
        
        messages.success(
                request, f'تهانينا {fname} لقد تمت عملية التسجيل بنجاح.')
        return HttpResponseRedirect('/login') 
    except:
        return HttpResponseRedirect('/register')


def log_in(request):
    if request.method == 'POST':
        form = log_in_form()
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')
    else:
        form = log_in_form()

    return render(request, 'user/log_in.html', {'title': 'تسجيل الدخول', 'form': form})

def log_out(request):
    logout(request)
    return render(request, 'user/log_out.html', {'title': 'تسجيل الخروج'})

# def log_in_backend(request):
#     u = request.POST['username']
#     p = request.POST['password']
#     au = authenticate(request, username = u, password = p)
#     if au is not None:
#         login(request, au)
#         return HttpResponseRedirect('/')
#     else:
#         messages.warning(request, 'هناك خطا في اسم المستخدم او كلمة المرور')
#         return HttpResponseRedirect('/login')

@login_required(login_url='login')
def profile(request):
    post_list = post.objects.filter(author = request.user)
    posts = post.objects.filter(author = request.user)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    return render(request, 'user/profile.html', {'title': 'الملف الشخصي','post_list': post_list ,'posts': posts, 'page': page})


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = user_update(request.POST, instance=request.user)
        image_form = image_update(request.POST, request.FILES, instance=request.user.pofile)
        if user_form.is_valid and image_form.is_valid:
            user_form.save()
            image_form.save()
            messages.success(
                    request, 'تم تعديل الملف الشخصي بنجاح .')
            return HttpResponseRedirect('/profile')
    else:
        user_form = user_update(instance=request.user)
        image_form = image_update(instance=request.user.pofile)
    return render(request, 'user/profile_update.html', {'title': 'تعديل الملف الشخصي', 'user': user_form, 'image': image_form})




    