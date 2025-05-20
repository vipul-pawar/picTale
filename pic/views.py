from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False) # Use this to create image instance to save author on dadtabase
            image.author = request.user
            form.save()
            return redirect('base')

    form = ImageForm()
    return render(request, 'pic/home.html',{'form':form})

def base(request):
    images = Image.objects.all()
    return render(request, 'pic/base.html',{'images':images})   

@login_required
def detailBlog(request, pk):
    images = get_object_or_404(Image, pk=pk)
    return render(request, 'pic/detailBlog.html', {'images': images})   

def team(request):
    return render(request, 'pic/team.html')

def contact(request):
    return render(request, 'pic/contact.html')

def delete(request,pk):
    images = get_object_or_404(Image, pk=pk)
    if request.method == 'GET':
        images.delete()
        return redirect('base')
    return render(request, 'pic/detailBlog.html', {'images': images})    