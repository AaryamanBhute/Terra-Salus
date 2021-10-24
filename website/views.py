from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from imageai.Classification import ImageClassification
import os
from django.conf import settings
from django.core.cache import cache


# Create your views here.
from .forms import *
from .models import *

def analyzeImage():

    execution_path = settings.BASE_DIR


    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
    prediction.loadModel()
    predictions, probabilities = prediction.classifyImage(os.path.join(settings.BASE_DIR, 'media/images/med.png'), result_count=10)
    r = []
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        if(eachProbability > 60):
            r.append(eachPrediction)
    items = Items.objects.all()
    print(r)
    for p in r:
        for i in items:
            if(p == i.name):
                link = "/information/" + p
                cache.clear()
                return(link)
    cache.clear()
    return('/None')
def success(request):
    return HttpResponse('successfully uploaded')
def home(request):
    return(render(request, "website/main.html"))
def about(request):
    return(render(request, "website/about.html"))
def contact(request):
    return(render(request, "website/contact.html"))
def future(request):
    return(render(request, "website/future.html"))
def none(request):
    return(render(request, "website/none.html"))
def use(request):
    if(request.method == 'POST'):
        form = ImageForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return(redirect(analyzeImage()))
    else:
        form = ImageForm()
    return(render(request, "website/use.html", {'form':form}))

def information(request, item_name):
    items = Items.objects.all()
    for i in items:
        if(i.name == item_name):
            item = i
            break
    it = {
        "item_data":item,
    }
    return(render(request, "website/information.html", it))
def spliter(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            for name in form.cleaned_data['names'].split(' '):
                Names(name = name).save()
                return HttpResponseRedirect('') # wherever you want to redirect
        return render(request, 'website/items.html', {'form': form})
    return render(request, 'website/items.html', {'form': ItemsForm()})