from django.shortcuts import render
from .models import Record
from .forms import RecordForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def cont(request):
    return render(request, 'main/cont.html')
def training(request):
    form = RecordForm()
    data={
        'form': form

    }
    return  render(request, 'main/training.html',data)