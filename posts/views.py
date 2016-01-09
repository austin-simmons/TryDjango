from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }
    return render(request, 'index.html', context)


def post_update(request):
    return HttpResponse('<h1>Update</h1>')


def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')
