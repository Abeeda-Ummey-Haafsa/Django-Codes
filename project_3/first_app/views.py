from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d ={'author': 'Rahim', 'age': 22, 'lst':['python', 'is', 'best'], 'birthday': datetime.datetime.now() , 'courses':[
        {'id': 1,
         'name': 'Python Programming',
         'fee': 5000
        },
        {'id': 2,
         'name': 'Django Programming',
         'fee': 10000
        },
    ]}
    return render(request, 'first_app/home.html', d)

# if you use the '' to initialize an integer then it's no longer 
#an integer. It becomes a string