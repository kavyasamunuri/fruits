from django.shortcuts import get_object_or_404, render

from quality.models import fruit
# Create your views here.
def fruit_details(request,pk):
    fruits=get_object_or_404(fruit,pk=pk)
    context={
        'fruits':fruits,
    }
    return render(request,'fruit_detail.html',context)