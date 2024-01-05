from django import forms 
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = StudentModel
        fields = '__all__'

        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }

        # widgets = {
        #     'roll' : forms.PasswordInput()
        # }

        help_texts = {
            'name' : "Write your full Name"
        }

        error_messages = {
            'name' : {'requried' : 'Your name is requried'}
        }
