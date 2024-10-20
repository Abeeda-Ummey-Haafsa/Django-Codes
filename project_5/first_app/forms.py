from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    file= forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField(label="User's Age")
    # weight = forms.FloatField(label="User's Weight")
    # balance = forms.DecimalField(label="User's Balance")
    # check = forms.BooleanField()
    # birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    # appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)

# Module 13.9 
# class StudentData(forms.Form):
#     name =forms.CharField(widget=forms.TextInput)
#     email =forms.CharField(widget=forms.EmailInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         valName = self.cleaned_data['name']
#         valEmail = self.cleaned_data['email']
#         if len(valName) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")    
#         if '.com' not in valEmail:
#             raise forms.ValidationError("Your email must contain .com")

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    email = forms.CharField(validators=[validators.EmailValidator(message='Enter a valid email address')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='Age must be maximum 34'), validators.MinValueValidator(24, message='age mus be minimum 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File extension must be .pdf')])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")