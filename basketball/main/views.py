from django.shortcuts import render, redirect
from .models import Record
from .forms import RecordForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    record=Record.objects.order_by('-level')
    return render(request, 'main/about.html',{'record':record})


def cont(request):
    return render(request, 'main/cont.html')


def training(request):
    error = ''
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = RecordForm()
    data = {
        'form':form ,
        'error': error

    }

    return render(request, 'main/training.html', data)