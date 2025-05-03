from django.shortcuts import render, redirect, get_object_or_404
from ..models import Crud
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    cruds= Crud.objects.all().order_by('-created_at')
    return render(request,'main/home.html',{'cruds':cruds})
def single_blog(request,crud_id):
    crud=get_object_or_404(Crud,pk=crud_id)
    return render(request,'main/single_blog.html',{'crud':crud})
def edit_blog(request, crud_id):
    crud = get_object_or_404(Crud, pk=crud_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        subTitle = request.POST.get('subTitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        crud.title = title
        crud.subTitle = subTitle
        crud.description = description
        
        if image:  
            crud.image = image

        crud.save()

        return redirect('crud_detail', crud_id=crud.id)

    return render(request, 'main/edit_blog.html', {'crud': crud})
# @login_required(login_url='/crud/login/')
def create_blog(request):
    if(request.method=='POST'):
        title=request.POST.get('title')
        subTitle=request.POST.get('subTitle')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        crud=Crud(title=title,subTitle=subTitle,description=description,image=image,author_id=request.user)
        crud.save()
        return redirect('/crud/')
    return render(request,'main/create_blog.html')
@login_required
def delete_blog(request, crud_id):
    blog = get_object_or_404(Crud, pk=crud_id)

    if request.method == 'POST':
        if blog.author_id == request.user:
             messages.success(request, "Blog deleted successfully.")
             blog.delete()
             return redirect('home')
        else:
            messages.warning(request, "You are not authorized to delete this blog.")
            return redirect('crud_detail', crud_id=crud_id)
    
      

