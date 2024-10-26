from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def DjangoForm(request):
    if request.method == 'POST':
        form = forms.practiceForm(request.POST)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./pracForms/uploads/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            # print(form.cleaned_data)
            form.save()
            return redirect('django_form')
    else:
        form = forms.practiceForm()
    return render(request, 'django_form.html', {'form':form}) 