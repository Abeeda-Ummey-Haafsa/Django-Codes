from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta: 
        model = StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']   # shows all except roll
        labels = {
            'name': 'Student Name',
            'roll': 'Roll Number'
        }
        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }
