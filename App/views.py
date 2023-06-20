from django.shortcuts import render
from django.http import HttpResponse
from .models import Foto,ImageCategory

# Create your views here.


def Home(request):
    image = Foto.objects.all()
    category = ImageCategory.objects.all()
    return render(request, 'App/index.html', {
        'images': image,
        'categorys': category
    })

def Galery(request):
    image = Foto.objects.all()
    category = ImageCategory.objects.all()
    return render(request, 'App/index.html', {
        'images': image,
        'categorys': category
    })
