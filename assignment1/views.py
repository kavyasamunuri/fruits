from django.shortcuts import render

from quality.models import fruit


def home(request):
    fruits=fruit.objects.all()
    context={
        'fruits':fruits,
    }

    return render(request,'home.html',context)