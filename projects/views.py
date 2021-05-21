from django.shortcuts import render, redirect
from .models import Project
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, slug):
    """
    pk = project id to load the correct project details 
    """
    project = Project.objects.get(slug=slug)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


@login_required(login_url="welcome")
def createpost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('project_index')
    context = {
        'form': form
    }
    return render(request, 'crud/post_form.html', context)


@login_required(login_url="welcome")
def updatepost(request, slug):
    post = Project.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('project_index')
    context = {
        'form': form
    }
    return render(request, 'crud/post_form.html', context)


@login_required(login_url="welcome")
def delete(request, slug):
    post = Project.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect('project_index')
    context = {'item': post}
    return render(request, 'crud/delete.html', context)
