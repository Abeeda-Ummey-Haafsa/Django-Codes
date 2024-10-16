from django.shortcuts import render
#E:\Phitron\Software Development\Week 3\Django Code\project_2\templates
def index(request):
    return render(request, 'index.html')