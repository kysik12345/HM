from django.shortcuts import render, get_object_or_404
from mysite.models import *
from mysite.forms import *
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator



# Create your views here.

def index(request):
    ads = Advertisement.objects.all().order_by('-created_at')
    paginator= Paginator(ads, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title':'Объявления'
    }
    return render(request, 'mysite/index.html', context)

def show(request, pk):
    ads = Advertisement.objects.get(pk=pk)
    context = {
        'ads': ads,
    }
    return render(request, 'mysite/show.html', context)

def about(request):
    context = {
        "name": "Анастасия",
        "lastname":"Попова",
        "email":"kysik123452mail.ru",
        "title":"О сайте",
    }
    return render(request, 'mysite/about.html',context=context)

def add(request):

    form = AdvertisementForm()

    if request.method == "POST":
        form = AdvertisementForm(data=request.POST)
        if form.is_valid():
            post= Advertisement()
            post.author = form.cleaned_data['author']
            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['description']
            post. price = form.cleaned_data['price']
           
            post.save()

            return index(request)

    context = {
        'form': form,
        'title':'Добавление объявления2'
    }
    return render(request, 'mysite/add.html', context)

def delete(request, pk):
    ads = Advertisement.objects.get(pk=pk)
    ads.delete()
    return render(request,'mysite/index.html')


def edit(request, pk):
    ads = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(data=request.POST, instance=ads)
        if form.is_valid():
            form.save()
            return show(request, pk)
    else:
        form = AdvertisementForm(instance=ads)

        context = {
            'form': form,
            'title': "Редактировать пост"
        }
        return render(request,'mysite/edit.html', context )
        


