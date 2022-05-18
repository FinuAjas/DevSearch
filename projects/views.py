from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from projects.forms import ProjectForm
from .models import Project

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    return render(request,'projects/projects.html',context)

def project(request,pk):
    project = Project.objects.get(id=pk)
    context = {
        'project':project,
    }
    return render(request,'projects/single-project.html',context)    

def createProject(request):
    forms = ProjectForm

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'forms':forms,
    }
    return render(request,'projects/project_form.html',context)    


def updateProject(request,pk):
    project = Project.objects.get(id = pk)
    forms = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'forms':forms,
    }
    return render(request,'projects/project_form.html',context)    

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'project':project,
    }
    return render(request,'projects/delete_template.html' ,context)    