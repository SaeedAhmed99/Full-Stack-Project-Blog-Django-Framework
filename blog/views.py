from django.shortcuts import render
from blog.models import post, comment
from . import models
from blog.forms import NewComment, CreatePost
from django.http import HttpResponseRedirect
from user.models import pofile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    po = post.objects.all()
    paginator = Paginator(po, 5)
    page = request.GET.get('page')
    try:
        po = paginator.page(page)
    except PageNotAnInteger:
        po = paginator.page(1)
    except EmptyPage:
        po = paginator.page(paginator.num_page)
    return render(request, 'blog/index.html', {'title': 'الصفحة الرئيسة', 'po': po, 'page': page})

def latest_pos(request):
    return render(request, 'latest_post.html', {})

def latest_com(request):
    return render(request, 'latest_comments.html', {})

def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})

def detail(request, post_id):
    po = models.post.objects.get(id = post_id)
    #com = comment.objects.filter(post_id = post_id, active = True)  Filter comments by activity status
    com = comment.objects.filter(post_id = post_id)
    # Function count that counts rows
    count = com.count()
    newcom = NewComment(request.POST or None)
    ob = comment()
    if newcom.is_valid():
        ob.post_id = post_id
        ob.name = newcom.cleaned_data['name']
        ob.email = newcom.cleaned_data['email']
        ob.body = newcom.cleaned_data['body']
        ob.save()
        return HttpResponseRedirect('/detail/' + str(post_id))

    context = {
        'title': po.title,
        'post': po,
        'comments': com,
        'count': count,
        'newcomment': newcom
    }
    return render(request, 'blog/detail.html', context)


class postCreateView(LoginRequiredMixin ,CreateView):
    model = post
    #   fields = ['title', 'content']
    template_name = 'blog/new_post.html'
    form_class = CreatePost


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

class postupdateView(UserPassesTestMixin, LoginRequiredMixin ,UpdateView):
    model = post
    #   fields = ['title', 'content']
    template_name = 'blog/postupdate.html'
    form_class = CreatePost


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False