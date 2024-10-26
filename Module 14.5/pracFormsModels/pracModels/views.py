from django.shortcuts import render, redirect, HttpResponse
from . import forms

# Create your views here.
def DjangoModel(request):
    if request.method == 'POST':
        model_form = forms.DjangoModels(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('django_model')
    else:
        model_form = forms.DjangoModels()
    return render(request, 'django_model.html', {'form': model_form})
    # return HttpResponse('models')