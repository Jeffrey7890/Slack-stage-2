from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('full_name','email', 'phone',
                    'address', 'skills', 'degree',
                    'school','accomplishments')
        widgets = {
            'full_name':forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter full name'}),
            'email':forms.TextInput(attrs = {'class':'form-control','placeholder':'Email'}),
            'phone':forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone number'}),
            'address':forms.Textarea(attrs = {'class':'form-control','placeholder':'Address'}),
            'skills':forms.TextInput(attrs = {'class':'form-control','placeholder':'Skills (comma seperated)'}),
            'degree':forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Degree'}),
            'school':forms.TextInput(attrs = {'class':'form-control','placeholder':'School'}),
            'accomplishments':forms.TextInput(attrs = {'class':'form-control','placeholder':'Accomplishments (comma seperated)'})

        }
